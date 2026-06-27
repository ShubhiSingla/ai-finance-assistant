from src.agents.finance_qa_agent import finance_qa_agent
from src.agents.market_agent import market_agent
from src.tools.market_data import get_stock_price
from src.agents.portfolio_agent import portfolio_agent
from src.tools.portfolio_tools import analyze_portfolio
from langchain_core.messages import ToolMessage
from src.agents.router_agent import router_agent
from src.agents.news_agent import news_agent
from src.tools.news_tools import fetch_news
from src.tools.yahoo_news import get_company_news


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

def news_agent_node(state):

    messages = state["chat_history"]

    response = news_agent.invoke(
        {
            "messages": messages
        }
    )

    if not response.tool_calls:
        return {
            "response": response.content
        }

    tool_call = response.tool_calls[0]
    tool_name = tool_call["name"]

    print(tool_call["args"])

    # Route to the correct tool
    if tool_name == "get_company_news":
        tool_result = get_company_news.invoke(tool_call["args"])
    elif tool_name == "fetch_news":
        tool_result = fetch_news.invoke(tool_call["args"])
    else:
        return {"response": f"Unknown tool: {tool_name}"}

    # Check for error in results (both tools return list with error dict)
    if isinstance(tool_result, list) and len(tool_result) > 0:
        if tool_result[0].get("status") == "error":
            return {
                "response": tool_result[0]["message"]
            }

    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )

    final_response = news_agent.invoke(
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