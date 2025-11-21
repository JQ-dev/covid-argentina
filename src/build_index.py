#!/usr/bin/env python3
"""
Build vector database index from ICD code data.
Creates embeddings and stores them in ChromaDB for efficient retrieval.
"""

from pathlib import Path
from typing import List, Dict
import pandas as pd

import click
from tqdm import tqdm
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma

from embeddings import get_embeddings


class VectorIndexBuilder:
    """Build vector database from medical code data."""

    def __init__(self, data_dir: Path = None):
        """Initialize the index builder."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.icd10cm_dir = self.data_dir / "icd10cm"
        self.vector_db_dir = self.data_dir / "vector_db"

        self.vector_db_dir.mkdir(parents=True, exist_ok=True)

    def load_icd10cm_codes(self) -> List[Document]:
        """
        Load ICD-10-CM codes from CSV.

        Returns:
            List of LangChain documents
        """
        csv_path = self.icd10cm_dir / "icd10cm_codes.csv"

        if not csv_path.exists():
            raise FileNotFoundError(
                f"ICD-10-CM codes not found at {csv_path}. "
                "Please run 'python src/data_loader.py' first."
            )

        print(f"Loading ICD-10-CM codes from {csv_path}...")
        df = pd.read_csv(csv_path)

        documents = []
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing codes"):
            # Create rich text representation for embedding
            text_parts = [
                f"Code: {row['code']}",
                f"Description: {row['description']}",
            ]

            if pd.notna(row.get('chapter')):
                text_parts.append(f"Chapter: {row['chapter']}")

            if pd.notna(row.get('includes')) and row['includes']:
                text_parts.append(f"Includes: {row['includes']}")

            if pd.notna(row.get('excludes')) and row['excludes']:
                text_parts.append(f"Excludes: {row['excludes']}")

            page_content = "\n".join(text_parts)

            # Create metadata
            metadata = {
                "code": row['code'],
                "description": row['description'],
                "code_system": row.get('code_system', 'ICD-10-CM'),
                "chapter": row.get('chapter', ''),
            }

            documents.append(Document(
                page_content=page_content,
                metadata=metadata
            ))

        print(f"✓ Loaded {len(documents)} ICD-10-CM codes")
        return documents

    def build_index(self, documents: List[Document], batch_size: int = 100):
        """
        Build vector index from documents.

        Args:
            documents: List of documents to index
            batch_size: Number of documents to process at once
        """
        print("\nBuilding vector index...")
        print(f"Total documents: {len(documents)}")
        print(f"Output directory: {self.vector_db_dir}")

        # Get embeddings model
        embeddings = get_embeddings(provider="sentence-transformers")

        # Build index in batches
        print("\nCreating embeddings and storing in ChromaDB...")

        # Create initial vectorstore with first batch
        vectorstore = Chroma.from_documents(
            documents=documents[:batch_size],
            embedding=embeddings,
            persist_directory=str(self.vector_db_dir)
        )

        # Add remaining documents in batches
        for i in tqdm(
            range(batch_size, len(documents), batch_size),
            desc="Indexing batches"
        ):
            batch = documents[i:i + batch_size]
            vectorstore.add_documents(batch)

        print(f"\n✓ Vector index built successfully!")
        print(f"  Location: {self.vector_db_dir}")
        print(f"  Total documents indexed: {len(documents)}")

    def verify_index(self):
        """Verify the index by running a test query."""
        print("\nVerifying index...")

        embeddings = get_embeddings(provider="sentence-transformers")
        vectorstore = Chroma(
            persist_directory=str(self.vector_db_dir),
            embedding_function=embeddings
        )

        # Test query
        test_query = "diabetes mellitus"
        results = vectorstore.similarity_search(test_query, k=3)

        print(f"\nTest query: '{test_query}'")
        print("Top 3 results:")
        for i, doc in enumerate(results, 1):
            print(f"\n{i}. {doc.metadata.get('code', 'N/A')} - {doc.metadata.get('description', 'N/A')}")

        print("\n✓ Index verification complete!")


@click.command()
@click.option('--data-dir', type=click.Path(), help='Custom data directory')
@click.option('--batch-size', default=100, help='Batch size for indexing')
@click.option('--verify', is_flag=True, help='Verify index after building')
def main(data_dir, batch_size, verify):
    """Build vector database index from ICD codes."""
    builder = VectorIndexBuilder(
        data_dir=Path(data_dir) if data_dir else None
    )

    # Load codes
    documents = builder.load_icd10cm_codes()

    # Build index
    builder.build_index(documents, batch_size=batch_size)

    # Verify if requested
    if verify:
        builder.verify_index()

    print("\n" + "=" * 60)
    print("Index building complete!")
    print("=" * 60)
    print("\nYou can now use the RAG system:")
    print("  python src/main.py query")


if __name__ == "__main__":
    main()
