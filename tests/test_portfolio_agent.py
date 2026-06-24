from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import HumanMessage

from src.agents.portfolio_agent import portfolio_agent
from src.tools.portfolio_tools import analyze_portfolio
from langchain_core.messages import ToolMessage


response = portfolio_agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="""
Analyze this portfolio:

{
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
"""
            )
        ]
    }
)

print(response.tool_calls)

tool_call = response.tool_calls[0]

tool_result = analyze_portfolio.invoke(
    tool_call["args"]
)

print(tool_result)

tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)

final_response = portfolio_agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="""
Analyze this portfolio:

{
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
"""
            ),
            response,
            tool_message
        ]
    }
)

print(final_response.content)