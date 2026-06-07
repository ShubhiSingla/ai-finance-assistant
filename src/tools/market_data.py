# Market Data Tool - fetches live and historical market data via external APIs
from langchain_core.tools import tool


@tool
def get_stock_price(ticker: str) -> dict:
    """Fetch the current price and basic info for a stock ticker.

    TODO: integrate with yfinance or Alpha Vantage API
    """
    # TODO: import yfinance as yf; return yf.Ticker(ticker).info
    raise NotImplementedError


@tool
def get_historical_data(ticker: str, period: str = "1mo") -> dict:
    """Fetch historical OHLCV data for a given ticker and time period.

    TODO: integrate with yfinance
    """
    raise NotImplementedError
