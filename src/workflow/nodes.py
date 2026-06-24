from src.agents.finance_qa_agent import finance_qa_agent
from src.agents.market_agent import market_agent
from src.tools.market_data import get_stock_price
from src.agents.portfolio_agent import portfolio_agent
from src.tools.portfolio_tools import analyze_portfolio
from langchain_core.messages import ToolMessage
from src.agents.router_agent import router_agent


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

    messages = state["chat_history"]

    messages = state["chat_history"]

    response = market_agent.invoke(
        {
            "messages": messages
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

    #If the tool returned an error, return it directly
    if tool_result["status"] == "error":
        return {
        "response": tool_result["message"]
        }
    

    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )

    final_response = market_agent.invoke(
        {
            "messages": messages + [
            response,
            tool_message
        ]
        }
    )

    return {
        "response": final_response.content
    }


def router_node(state):

    messages = state["chat_history"]

    response = router_agent.invoke(
        {
            "messages": messages
        }
    )

    route = response.content.strip()

    print("Router selected:", route)

    return {
        "route": route
    }

def portfolio_agent_node(state):

    messages = state["chat_history"]

    response = portfolio_agent.invoke(
        {
            "messages": messages
        }
    )

    if not response.tool_calls:
        return {
            "response": response.content
        }

    tool_call = response.tool_calls[0]

    tool_result = analyze_portfolio.invoke(
        tool_call["args"]
    )

    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )

    final_response = portfolio_agent.invoke(
        {
            "messages": messages + [
            response,
            tool_message
        ]
        }
    )

    return {
        "response": final_response.content
    }