from langchain_core.tools import tool


@tool
def analyze_portfolio(portfolio: dict) -> dict:
    """
    Analyze a user's investment portfolio.

    Args:
        portfolio:
        {
            "AAPL": {
                "quantity": 10,
                "current_price": 290.50
            },
            "TSLA": {
                "quantity": 5,
                "current_price": 320.75
            }
        }

    Returns:
        Dictionary containing:
        - Total portfolio value
        - Allocation percentage of each holding
    """

    # Empty portfolio
    if not portfolio:
        return {
            "total_value": 0,
            "allocation": {}
        }

    # Calculate total portfolio value
    total_value = 0

    for holding in portfolio.values():
        quantity = holding.get("quantity", holding.get("shares"))
        total_value += (
            quantity * holding["current_price"]
        )

    # Prevent division by zero
    if total_value == 0:
        return {
            "total_value": 0,
            "allocation": {}
        }

    allocation = {}

    for ticker, holding in portfolio.items():

        quantity = holding.get("quantity", holding.get("shares", 0))
        value = quantity * holding["current_price"]

        allocation[ticker] = {
            "quantity": quantity,
            "current_price": holding["current_price"],
            "value": round(value, 2),
            "allocation_pct": round(
                (value / total_value) * 100,
                2
            )
        }

    return {
        "total_value": round(total_value, 2),
        "allocation": allocation
    }