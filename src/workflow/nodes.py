from langchain_core.messages import HumanMessage
from langchain_core.messages import ToolMessage

from src.agents.finance_qa_agent import finance_qa_agent
from src.agents.market_agent import market_agent
from src.tools.market_data import get_stock_price


def finance_qa_node(state):

    query = state["user_query"]

    vector_store = state["vector_store"]

    response = finance_qa_agent(
        query,
        vector_store
    )

    return {
        "response": response
    }


def market_agent_node(state):

    query = state["user_query"]

    response = market_agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=query
                )
            ]
        }
    )

    if not response.tool_calls:
        return {
            "response": response.content
        }

    tool_call = response.tool_calls[0]

    tool_result = get_stock_price.invoke(
        tool_call["args"]
    )

    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )

    final_response = market_agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=query
                ),
                response,
                tool_message
            ]
        }
    )

    return {
        "response": final_response.content
    }


def router_node(state):

    query = state["user_query"].lower()

    market_keywords = [
        "stock",
        "share",
        "price",
        "ticker",
        "market",
        "apple",
        "tesla",
        "aapl",
        "tsla",
        "nvda",
        "nvidia"
    ]

    for keyword in market_keywords:
        if keyword in query:
            return {
                "route": "market_agent"
            }

    return {
        "route": "finance_qa"
    }