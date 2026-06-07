# News Fetcher - retrieves financial news from external APIs or RSS feeds
from langchain_core.tools import tool


@tool
def fetch_news(topic: str, max_articles: int = 5) -> list[dict]:
    """Fetch recent financial news articles for a given topic or ticker.

    TODO: integrate with NewsAPI, Alpha Vantage News, or RSS feed
    """
    # TODO: call news API, return list of {"title": ..., "url": ..., "summary": ...}
    raise NotImplementedError
