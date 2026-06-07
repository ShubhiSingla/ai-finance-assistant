# Tax Agent - answers tax-related questions and provides guidance


class TaxAgent:
    """Provides tax planning guidance and answers tax-related queries using RAG."""

    def __init__(self, retriever, llm):
        # TODO: initialize retriever (tax documents) and LLM
        self.retriever = retriever
        self.llm = llm

    def run(self, query: str) -> str:
        # TODO: retrieve relevant tax docs and generate response
        raise NotImplementedError
