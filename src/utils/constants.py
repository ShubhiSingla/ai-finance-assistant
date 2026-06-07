# Constants - application-wide constant values

# Agent route identifiers
ROUTE_FINANCE_QA = "finance_qa"
ROUTE_PORTFOLIO = "portfolio"
ROUTE_MARKET = "market"
ROUTE_GOAL_PLANNER = "goal_planner"
ROUTE_NEWS = "news"
ROUTE_TAX = "tax"
ROUTE_COMPLIANCE = "compliance"

ALL_ROUTES = [
    ROUTE_FINANCE_QA,
    ROUTE_PORTFOLIO,
    ROUTE_MARKET,
    ROUTE_GOAL_PLANNER,
    ROUTE_NEWS,
    ROUTE_TAX,
    ROUTE_COMPLIANCE,
]

# RAG defaults
DEFAULT_CHUNK_SIZE = 512
DEFAULT_CHUNK_OVERLAP = 64
DEFAULT_TOP_K = 5

# Supported document extensions
SUPPORTED_DOC_EXTENSIONS = [".pdf", ".txt", ".md"]
