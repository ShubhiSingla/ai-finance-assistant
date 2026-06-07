# main.py - CLI entry point to run the AI Finance Assistant workflow
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Run the finance assistant with a sample query."""
    # TODO: build graph and invoke
    # from src.workflow.graph import build_graph
    # graph = build_graph()
    # result = graph.invoke({"query": "What is dollar-cost averaging?"})
    # print(result["response"])
    logger.info("AI Finance Assistant starting up...")
    print("🚧 Workflow not yet wired. Implement graph.py to get started.")


if __name__ == "__main__":
    main()
