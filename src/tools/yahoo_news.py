# Yahoo Finance News - fetches company-specific financial news
import yfinance as yf
from langchain_core.tools import tool


@tool
def get_company_news(ticker: str, max_articles: int = 5) -> list[dict]:
    """Fetch recent financial news for a specific company ticker using Yahoo Finance.

    Args:
        ticker: stock ticker symbol (e.g., 'AAPL', 'TSLA', 'MSFT', 'TCS.NS')
        max_articles: maximum number of articles to return (default 5)

    Returns:
        List of dicts with title, publisher, link, and publish time.
        Returns an error message if ticker is invalid or no news is found.
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news

        if not news or len(news) == 0:
            return [{
                "status": "error",
                "message": f"No news available for '{ticker}'. This ticker may not have recent news coverage on Yahoo Finance."
            }]

        articles = []
        for article in news[:max_articles]:
            try:
                # Extract content from nested structure
                content = article.get("content", {})
                
                title = content.get("title", "No title")
                publisher = content.get("provider", {}).get("displayName", "Unknown")
                link = content.get("clickThroughUrl", {}).get("url", "")
                published = content.get("pubDate", "")
                summary = content.get("summary", "")
                
                articles.append({
                    "title": title,
                    "publisher": publisher,
                    "link": link,
                    "published_at": published,
                    "summary": summary
                })
            except Exception as parse_error:
                continue  # Skip malformed articles
        
        if not articles:
            return [{
                "status": "error",
                "message": f"Could not parse news articles for '{ticker}'."
            }]
        
        return articles

    except Exception as e:
        return [{
            "status": "error",
            "message": f"Failed to fetch news for '{ticker}': {str(e)}"
        }]
