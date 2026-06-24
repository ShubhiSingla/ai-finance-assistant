from src.tools.portfolio_tools import analyze_portfolio

portfolio = {
    "AAPL": {
        "quantity": 10,
        "current_price": 290
    },
    "TSLA": {
        "quantity": 5,
        "current_price": 320
    },
    "NVDA": {
        "quantity": 8,
        "current_price": 170
    }
}

result = analyze_portfolio.invoke(
    {
        "portfolio": portfolio
    }
)

print(result)