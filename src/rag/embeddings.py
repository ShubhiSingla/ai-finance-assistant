# Embeddings - wraps embedding model for converting text chunks to vectors


def get_embedding_model(model_name: str = "text-embedding-3-small"):
    """Initialize and return the embedding model.

    TODO: support OpenAI, HuggingFace, or Bedrock embeddings
    """
    # TODO: from langchain_openai import OpenAIEmbeddings
    raise NotImplementedError
