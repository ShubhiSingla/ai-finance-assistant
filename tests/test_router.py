from dotenv import load_dotenv

load_dotenv()
from src.workflow.nodes import router_node


def test_stock_query_routes_to_market():
    result = router_node({
        "user_query": "What is Apple stock price?"
    })

    assert result["route"] == "market_agent"

def test_sip_query_routes_to_finance():

    result = router_node(
        {
            "user_query": "What is SIP?"
        }
    )

    assert result["route"] == "finance_qa"    