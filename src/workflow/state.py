#creating state - state allows: nodes to communicate, multi-agent orchestration
from typing import TypedDict #defines structure of dictionary
from typing import List, Any

from langchain_core.messages import BaseMessage


class FinanceAgentState(TypedDict):

    user_query: str

    chat_history: List[BaseMessage]

    response: str

    vector_store: Any

    route: str