# Finance Q&A Agent - answers general finance questions using RAG + LLM
from langchain_core.messages import BaseMessage


class FinanceQAAgent:
    """Handles general financial Q&A using RAG-augmented generation."""

    def __init__(self, retriever, llm):
        # TODO: initialize retriever and LLM
        self.retriever = retriever
        self.llm = llm

    def run(self, query: str) -> str:
        # TODO: retrieve context, build prompt, invoke LLM
        raise NotImplementedError
