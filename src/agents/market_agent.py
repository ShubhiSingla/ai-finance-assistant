from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from src.tools.market_data import get_stock_price

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.2
)


market_agent_prompt = ChatPromptTemplate.from_messages([

    ("system", """
You are a financial market intelligence assistant.

Your job is to help users with:
- stock prices
- company information
- market trends
- ETF information
- investment-related market queries

Rules:
- Use available tools whenever live market data is needed.
- Always provide accurate and concise responses.
- Explain financial information in easy english, beginner-friendly language.
- If a query is unrelated to financial markets, politely refuse.

When responding, include:
- company name
- stock ticker
- stock price
- currency
- short explanation if useful
"""),

    MessagesPlaceholder(variable_name="messages")

])

llm_with_stock_price_tools = llm.bind_tools([get_stock_price])

market_agent = market_agent_prompt | llm_with_stock_price_tools