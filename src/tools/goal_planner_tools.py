from langchain_core.tools import tool


@tool
def calculate_goal_plan(
    goal_amount: float,
    years: int,
    annual_return: float = 12.0
) -> dict:
    """
    Calculates the monthly SIP required to achieve a financial goal.

    Args:
        goal_amount: Target amount the user wants to accumulate.
        years: Investment duration in years.
        annual_return: Expected annual return percentage.
                       Defaults to 12%.

    Returns:
        A dictionary containing:

        - status
        - goal_amount
        - target_corpus
        - years
        - annual_return
        - monthly_sip
    """

    # Validate inputs
    if goal_amount <= 0:
        return {
            "status": "error",
            "message": "Goal amount must be greater than 0."
        }

    if years <= 0:
        return {
            "status": "error",
            "message": "Investment duration must be greater than 0 years."
        }

    if annual_return <= 0:
        return {
            "status": "error",
            "message": "Annual return must be greater than 0."
        }

    # Convert annual return to monthly return
    monthly_rate = annual_return / (12 * 100)

    # Total investment months
    months = years * 12

    # Calculate required monthly SIP
    monthly_sip = (
        goal_amount
        * monthly_rate
        / (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate))
    )

    return {
        "status": "success",
        "goal_amount": goal_amount,
        "target_corpus": goal_amount,
        "years": years,
        "annual_return": annual_return,
        "monthly_sip": round(monthly_sip, 2)
    }