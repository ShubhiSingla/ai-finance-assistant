# Yahoo Finance News - fetches company-specific financial news
import yfinance as yf
from langchain_core.tools import tool


@tool
def get_company_news(ticker: str, max_articles: int = 5) -> list[dict]:
    """Fetch recent financial news for a specific company ticker using Yahoo Finance.

    Args:
        ticker: stock ticker symbol (e.g., 'AAPL', 'TSLA', 'MSFT')
        max_articles: maximum number of articles to return (default 5)

    Returns:
        List of dicts with title, publisher, link, and publish time.
        Returns an error message if ticker is invalid or no news is found.
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news

        if not news:
            return [{
                "status": "error",
                "message": f"No news found for ticker '{ticker}'. Verify the ticker is correct."
            }]

        articles = []
        for article in news[:max_articles]:
            # Yahoo Finance news structure has nested 'content' field
            content = article.get("content", {})
            provider = article.get("provider", {})
            
            articles.append({
                "title": content.get("title"),
                "publisher": provider.get("displayName"),
                "link": article.get("clickThroughUrl", {}).get("url"),
                "published_at": content.get("pubDate"),
                "summary": content.get("summary")
            })
        
        return articles

    except Exception as e:
        return [{
            "status": "error",
            "message": f"Failed to fetch news for '{ticker}': {str(e)}"
        }]
