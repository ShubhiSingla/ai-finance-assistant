# Market Agent - fetches and interprets live/historical market data


class MarketAgent:
    """Handles market data queries, trend analysis, and stock lookups."""

    def __init__(self, llm, market_data_tool):
        # TODO: initialize LLM and market data tool
        self.llm = llm
        self.market_data_tool = market_data_tool

    def run(self, query: str) -> str:
        # TODO: fetch market data and generate natural language summary
        raise NotImplementedError
