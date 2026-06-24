import yfinance as yf
from yfinance.exceptions import YFRateLimitError
from langchain_core.tools import tool


@tool
def get_stock_price(ticker: str) -> dict:
    """
    Fetch the latest stock price and basic company information.
    """

    try:
        info = yf.Ticker(ticker).info

        # Check if stock data exists
        if not info or info.get("currentPrice") is None:
            return {
                "status": "error",
                "message": f"Could not find stock information for ticker '{ticker}'."
            }

        return {
            "status": "success",
            "ticker": ticker.upper(),
            "company": info.get("shortName"),
            "current_price": info.get("currentPrice"),
            "currency": info.get("currency")
        }

    except YFRateLimitError:
        return {
            "status": "error",
            "message": (
                "Yahoo Finance is temporarily rate limiting requests. "
                "Please try again in a few minutes."
            )
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Unable to fetch stock data: {str(e)}"
        }