# Ingest - loads raw documents from disk or external sources into the pipeline
from pathlib import Path


def load_documents(source_dir: str) -> list:
    """Load raw documents from a directory.

    Supports PDF, TXT, and Markdown files.
    TODO: implement loaders using LangChain document loaders
    """
    # TODO: use langchain_community.document_loaders (PyPDFLoader, TextLoader, etc.)
    raise NotImplementedError
