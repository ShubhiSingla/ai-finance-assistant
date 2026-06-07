# Graph - defines the LangGraph StateGraph connecting all agent nodes
from langgraph.graph import StateGraph, END
from src.workflow.state import AssistantState


def build_graph() -> StateGraph:
    """Build and compile the LangGraph workflow.

    Nodes: router → [finance_qa | portfolio | market | goal_planner | news | tax | compliance]
    TODO: add nodes, edges, and conditional routing logic
    """
    graph = StateGraph(AssistantState)

    # TODO: graph.add_node(...)
    # TODO: graph.add_conditional_edges(...)
    # TODO: graph.set_entry_point("router")

    return graph.compile()
