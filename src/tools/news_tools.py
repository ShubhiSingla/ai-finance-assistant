# News Fetcher - retrieves financial news from NewsAPI
import os
from langchain_core.tools import tool
from newsapi import NewsApiClient


@tool
def fetch_news(topic: str, max_articles: int = 5) -> list[dict]:
    """Fetch recent financial news articles for a given topic or ticker.

    Args:
        topic: company name, ticker, or financial topic to search.
               Include finance-specific keywords like 'earnings', 'stock', 'revenue', 'market'
               to improve relevancy. Example: 'Apple earnings stock' instead of just 'Apple'.
        max_articles: maximum number of articles to return (default 5)

    Returns:
        List of dicts with title, url, and description.
        Returns an empty list with a message if no news is found.
    """
    try:
        api_key = os.getenv("NEWS_API_KEY")

        if not api_key:
            return [{"status": "error", "message": "NEWS_API_KEY is not set."}]

        newsapi = NewsApiClient(api_key=api_key)

        # Financial news sources only
        financial_domains = [
            "bloomberg.com",
            "reuters.com",
            "wsj.com",
            "ft.com",
            "cnbc.com",
            "marketwatch.com",
            "seekingalpha.com",
            "fool.com",
            "barrons.com",
            "investors.com"
        ]

        response = newsapi.get_everything(
            q=topic,
            language="en",
            sort_by="relevancy",
            page_size=max_articles,
            domains=",".join(financial_domains)
        )

        articles = response.get("articles", [])

        if not articles:
            return [{"status": "error", "message": f"No news found for '{topic}'."}]

        return [
            {
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "description": article.get("description"),
                "published_at": article.get("publishedAt")
            }
            for article in articles
        ]

    except Exception as e:
        return [{"status": "error", "message": f"Failed to fetch news: {str(e)}"}]
