import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

@tool
def get_news(query: str) -> dict:
    """
    Fetches news articles related to a given query using the NewsAPI.
    """

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        if data["status"] != "ok":
            return {"status": "error", "message": "Failed to fetch news."}

        articles = data.get("articles", [])[:5]  # Limit to top 5 articles
        if not articles:
            return {
                "status": "error",
                "message": f"No news found for '{query}'."
            }

        formatted_articles = [
            {
                "title": article["title"],
                "description": article["description"],
                "source": article["source"]["name"],
                "publishedAt": article["publishedAt"]
                "url": article["url"]
            }
            for article in articles
        ]

        return {
            "status": "success",
            "query": query,
            "articles": formatted_articles
        }

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}



