import yfinance as yf
from langchain_core.tools import tool

@tool
def get_stock_price(ticker: str) -> dict:
    """Fetch the current price and basic info for a stock ticker."""

    info = yf.Ticker(ticker).info
    return {
        "ticker": ticker,
        "price": info.get("currentPrice"),
        "name": info.get("shortName"),
        "currency": info.get("currency"),
    }


