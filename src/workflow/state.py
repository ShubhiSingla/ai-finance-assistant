# State - defines the shared LangGraph state schema passed between nodes
from typing import Annotated, Any
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class AssistantState(TypedDict):
    """Shared state object flowing through the LangGraph workflow."""

    query: str                          # original user query
    messages: Annotated[list, add_messages]  # conversation history
    route: str                          # resolved agent route
    context: list[str]                  # retrieved RAG documents
    response: str                       # final agent response
    metadata: dict[str, Any]            # optional extras (user profile, portfolio id, etc.)
