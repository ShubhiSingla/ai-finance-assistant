# Portfolio Utils - helper functions for portfolio analysis and metrics
from langchain_core.tools import tool


@tool
def analyze_portfolio(portfolio: dict) -> dict:
    """
    Analyze portfolio allocation.

    Args:
        portfolio: dict of {ticker: {"shares": int, "current_price": float}}
    """
    # 1. Calculate total value
    total_value = sum(
        v["shares"] * v["current_price"] for v in portfolio.values()
    )

    # 2. Calculate allocation %
    allocation = {
        ticker: {
            "value": data["shares"] * data["current_price"],
            "allocation_pct": round((data["shares"] * data["current_price"]) / total_value * 100, 2)
        }
        for ticker, data in portfolio.items()
    }

    # 3. Return dictionary
    return {"total_value": total_value, "allocation": allocation}


@tool
def calculate_portfolio_return(holdings: dict) -> float:
    """Calculate the overall return of a portfolio given holdings.

    Args:
        holdings: dict of {ticker: {"shares": int, "avg_cost": float}}
    TODO: fetch current prices and compute weighted return
    """
    raise NotImplementedError


@tool
def get_asset_allocation(holdings: dict) -> dict:
    """Return asset class breakdown of a portfolio.

    TODO: classify each ticker into equity/bond/cash/alternative
    """
    raise NotImplementedError
