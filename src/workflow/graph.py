from langgraph.graph import StateGraph
from langgraph.graph import START, END

from src.workflow.state import FinanceAgentState
from src.workflow.nodes import (
    finance_qa_node,
    market_agent_node,
    router_node
    )


def build_graph():

    graph_builder = StateGraph(FinanceAgentState)

    graph_builder.add_node(
    "router",
    router_node
    )

    # Add node
    graph_builder.add_node(
        "finance_qa",
        finance_qa_node
    )

    graph_builder.add_node(
        "market_agent",
        market_agent_node
    )

    graph_builder.add_edge(
    START,
    "router"
    )

    graph_builder.add_conditional_edges(
        "router",
        lambda state: state["route"],
        {
            "finance_qa": "finance_qa",
            "market_agent": "market_agent"
        }
    )

    graph_builder.add_edge(
        "finance_qa",
        END
    )

    graph_builder.add_edge(
        "market_agent",
        END
    )

    graph = graph_builder.compile()

    return graph