# Calculator - financial math utilities (compound interest, SIP, EMI, etc.)
from langchain_core.tools import tool


@tool
def compound_interest(principal: float, rate: float, years: int, n: int = 12) -> float:
    """Calculate compound interest.

    Formula: A = P(1 + r/n)^(nt)
    TODO: implement formula
    """
    raise NotImplementedError


@tool
def sip_future_value(monthly_investment: float, annual_rate: float, years: int) -> float:
    """Calculate future value of a monthly SIP investment.

    TODO: implement SIP future value formula
    """
    raise NotImplementedError


@tool
def emi_calculator(principal: float, annual_rate: float, months: int) -> float:
    """Calculate EMI for a loan.

    Formula: EMI = P * r * (1+r)^n / ((1+r)^n - 1)
    TODO: implement EMI formula
    """
    raise NotImplementedError
