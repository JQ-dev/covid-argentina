"""
Embedding generation for medical codes.
Uses specialized medical domain embeddings for better semantic understanding.
"""

from typing import Optional

from langchain_openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer


class MedicalEmbeddings:
    """Wrapper for medical domain embeddings."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize medical embeddings.

        Args:
            model_name: Name of the sentence transformer model
        """
        # Use a medical-domain model if available, fallback to general purpose
        # Options: 'all-MiniLM-L6-v2', 'pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb'
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """
        Embed a list of documents.

        Args:
            texts: List of text documents to embed

        Returns:
            List of embedding vectors
        """
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()

    def embed_query(self, text: str) -> list[float]:
        """
        Embed a single query.

        Args:
            text: Query text to embed

        Returns:
            Embedding vector
        """
        embedding = self.model.encode([text])[0]
        return embedding.tolist()


def get_embeddings(provider: str = "sentence-transformers") -> any:
    """
    Get embeddings model based on provider.

    Args:
        provider: Embedding provider ('openai' or 'sentence-transformers')

    Returns:
        Embeddings model instance
    """
    if provider == "openai":
        return OpenAIEmbeddings(model="text-embedding-3-small")
    elif provider == "sentence-transformers":
        return MedicalEmbeddings(model_name="all-MiniLM-L6-v2")
    else:
        raise ValueError(f"Unsupported embedding provider: {provider}")
