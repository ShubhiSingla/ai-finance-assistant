# Nodes - LangGraph node functions that wrap each agent's run() method
from src.workflow.state import AssistantState


def finance_qa_node(state: AssistantState) -> AssistantState:
    # TODO: initialize FinanceQAAgent and invoke with state["query"]
    raise NotImplementedError


def portfolio_node(state: AssistantState) -> AssistantState:
    # TODO: initialize PortfolioAgent and invoke with state["metadata"]["portfolio"]
    raise NotImplementedError


def market_node(state: AssistantState) -> AssistantState:
    # TODO: initialize MarketAgent and invoke with state["query"]
    raise NotImplementedError


def goal_planner_node(state: AssistantState) -> AssistantState:
    # TODO: initialize GoalPlannerAgent and invoke with state["metadata"]["goals"]
    raise NotImplementedError


def news_node(state: AssistantState) -> AssistantState:
    # TODO: initialize NewsAgent and invoke with state["query"]
    raise NotImplementedError


def tax_node(state: AssistantState) -> AssistantState:
    # TODO: initialize TaxAgent and invoke with state["query"]
    raise NotImplementedError


def compliance_node(state: AssistantState) -> AssistantState:
    # TODO: initialize ComplianceAgent and invoke with state["query"]
    raise NotImplementedError
