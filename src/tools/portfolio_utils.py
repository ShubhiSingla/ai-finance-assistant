# Portfolio Utils - helper functions for portfolio analysis and metrics
from langchain_core.tools import tool


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
