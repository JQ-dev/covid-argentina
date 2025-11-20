"""
Core RAG system for medical coding.
Handles query processing, retrieval, and code generation.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Any

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic

from embeddings import get_embeddings


class MedicalCodingRAG:
    """RAG system for medical code retrieval and recommendations."""

    def __init__(
        self,
        data_dir: Optional[Path] = None,
        llm_provider: str = "openai",
        model_name: Optional[str] = None
    ):
        """
        Initialize the Medical Coding RAG system.

        Args:
            data_dir: Directory containing the vector database
            llm_provider: LLM provider to use ('openai' or 'anthropic')
            model_name: Specific model name (optional)
        """
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.vector_db_dir = self.data_dir / "vector_db"

        if not self.vector_db_dir.exists():
            raise FileNotFoundError(
                f"Vector database not found at {self.vector_db_dir}. "
                "Please run 'python src/build_index.py' first."
            )

        # Initialize embeddings
        self.embeddings = get_embeddings()

        # Initialize vector store
        self.vectorstore = Chroma(
            persist_directory=str(self.vector_db_dir),
            embedding_function=self.embeddings
        )

        # Initialize LLM
        if llm_provider == "openai":
            self.llm = ChatOpenAI(
                model_name=model_name or "gpt-4-turbo-preview",
                temperature=0.1
            )
        elif llm_provider == "anthropic":
            self.llm = ChatAnthropic(
                model=model_name or "claude-3-sonnet-20240229",
                temperature=0.1
            )
        else:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")

        # Create retrieval chain
        self.qa_chain = self._create_qa_chain()

    def _create_qa_chain(self) -> RetrievalQA:
        """Create the question-answering chain."""
        prompt_template = """You are an expert medical coder with deep knowledge of ICD-10-CM, ICD-10-PCS, CPT, and HCPCS coding systems.

Based on the following context from official coding manuals and guidelines, provide accurate medical codes for the query.

Context:
{context}

Query: {question}

Please provide:
1. The most appropriate primary code(s)
2. A clear description of what the code represents
3. Any relevant coding guidelines or notes
4. Related or alternative codes that might be relevant
5. Important coding considerations (e.g., sequencing, combination codes, excludes notes)

Format your response as a structured JSON with the following fields:
- primary_code: The main code(s) to use
- description: Clear description of the code
- code_system: Which coding system (ICD-10-CM, ICD-10-PCS, etc.)
- guidelines: Relevant coding guidelines
- related_codes: List of related codes with descriptions
- considerations: Important notes for proper code assignment

Answer:"""

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": 5}
            ),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )

        return qa_chain

    def query(
        self,
        query: str,
        code_system: str = "all",
        include_sources: bool = False
    ) -> Dict[str, Any]:
        """
        Query the RAG system for medical codes.

        Args:
            query: The medical condition or procedure to look up
            code_system: Filter by code system ('icd10cm', 'icd10pcs', 'all')
            include_sources: Include source documents in response

        Returns:
            Dictionary containing codes, descriptions, and guidelines
        """
        try:
            # Add code system filter to query if specified
            if code_system != "all":
                enhanced_query = f"{query} (code system: {code_system.upper()})"
            else:
                enhanced_query = query

            # Run the query
            result = self.qa_chain.invoke({"query": enhanced_query})

            # Parse the response
            response = self._parse_response(result["result"])

            # Add source documents if requested
            if include_sources:
                response["sources"] = [
                    {
                        "content": doc.page_content,
                        "metadata": doc.metadata
                    }
                    for doc in result.get("source_documents", [])
                ]

            # Add confidence score based on retrieval similarity
            if "source_documents" in result and result["source_documents"]:
                # Simple confidence based on number of relevant documents found
                response["confidence"] = min(
                    len(result["source_documents"]) / 5.0,
                    1.0
                )

            return response

        except Exception as e:
            return {
                "error": str(e),
                "query": query
            }

    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """
        Parse the LLM response into structured format.

        Args:
            response_text: Raw text response from LLM

        Returns:
            Structured dictionary with code information
        """
        import json
        import re

        # Try to extract JSON from response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)

        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        # Fallback: Parse as structured text
        result = {
            "primary_code": self._extract_field(response_text, "primary_code"),
            "description": self._extract_field(response_text, "description"),
            "code_system": self._extract_field(response_text, "code_system"),
            "guidelines": self._extract_field(response_text, "guidelines"),
            "related_codes": self._extract_related_codes(response_text),
            "considerations": self._extract_field(response_text, "considerations")
        }

        return result

    def _extract_field(self, text: str, field_name: str) -> str:
        """Extract a field value from structured text."""
        import re

        pattern = rf"{field_name}[:\s]+(.+?)(?=\n[a-z_]+:|$)"
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

        if match:
            return match.group(1).strip()

        return "N/A"

    def _extract_related_codes(self, text: str) -> List[Dict[str, str]]:
        """Extract related codes from response text."""
        # Simplified extraction - can be enhanced
        import re

        codes = []
        pattern = r'([A-Z]\d{2}(?:\.\d{1,4})?)\s*[-:]\s*(.+?)(?=\n|$)'

        for match in re.finditer(pattern, text):
            codes.append({
                "code": match.group(1),
                "description": match.group(2).strip()
            })

        return codes[:5]  # Return top 5 related codes

    def search_by_code(self, code: str) -> Dict[str, Any]:
        """
        Look up information for a specific code.

        Args:
            code: The medical code to look up (e.g., "J44.1")

        Returns:
            Dictionary with code details
        """
        return self.query(f"What is medical code {code}?")

    def get_coding_guidelines(self, condition: str) -> str:
        """
        Get coding guidelines for a specific condition.

        Args:
            condition: Medical condition or category

        Returns:
            Coding guidelines text
        """
        result = self.query(f"What are the coding guidelines for {condition}?")
        return result.get("guidelines", "No guidelines found")
