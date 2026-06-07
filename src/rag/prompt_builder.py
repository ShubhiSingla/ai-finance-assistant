# Prompt Builder - constructs LLM prompts from retrieved context and user query
from langchain_core.prompts import ChatPromptTemplate


def build_rag_prompt(context: str, query: str) -> ChatPromptTemplate:
    """Build a RAG prompt template combining retrieved context and user query.

    TODO: customize system message and prompt template per agent type
    """
    # TODO: define system prompt with finance-specific instructions
    raise NotImplementedError
