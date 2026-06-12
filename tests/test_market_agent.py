from dotenv import load_dotenv

load_dotenv()
from src.tools.market_data import get_stock_price


def test_stock_price():
    result = get_stock_price.invoke(
        {"ticker": "AAPL"}
    )

    assert result["ticker"] == "AAPL"