from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage

from src.agents.market_agent import market_agent
from src.tools.market_data import get_stock_price
from langchain_core.messages import ToolMessage


response = market_agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is Apple stock price?"
            )
        ]
    }
)
print(response.tool_calls)

tool_call = response.tool_calls[0]

tool_result = get_stock_price.invoke(
    tool_call["args"]
)

print(tool_result)
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)

print(tool_message)

final_response = market_agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="What is Apple stock price?"
            ),
            response,
            tool_message
        ]
    }
)

print(final_response.content)