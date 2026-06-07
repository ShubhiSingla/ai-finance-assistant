# Router - classifies incoming user queries and routes to the correct agent node
from src.workflow.state import AssistantState

# Supported agent route keys
ROUTES = ["finance_qa", "portfolio", "market", "goal_planner", "news", "tax", "compliance"]


def route_query(state: AssistantState) -> str:
    """Classify the user query and return the target agent node name.

    TODO: use LLM-based intent classification or keyword matching
    """
    # TODO: implement routing logic based on state["query"]
    raise NotImplementedError
