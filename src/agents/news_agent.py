# News Agent - fetches and summarizes financial news


class NewsAgent:
    """Retrieves and summarizes relevant financial news for a given topic or asset."""

    def __init__(self, llm, news_fetcher):
        # TODO: initialize LLM and news fetcher tool
        self.llm = llm
        self.news_fetcher = news_fetcher

    def run(self, topic: str) -> str:
        # TODO: fetch news articles and return LLM-generated summary
        raise NotImplementedError
