# Vector Store - manages storage and retrieval of document embeddings


def build_vector_store(chunks: list, embedding_model):
    """Create and persist a vector store from document chunks.

    TODO: support FAISS, Chroma, or Pinecone backends
    """
    # TODO: from langchain_community.vectorstores import FAISS
    raise NotImplementedError


def load_vector_store(path: str, embedding_model):
    """Load an existing vector store from disk.

    TODO: implement persistent store loading
    """
    raise NotImplementedError
