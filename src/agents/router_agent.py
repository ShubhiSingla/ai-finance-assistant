from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

router_agent_prompt = ChatPromptTemplate.from_messages([

    ("system", """
You are an intelligent routing agent.

Your only job is to decide which specialized agent should answer the user's request.

Available agents:

1. finance_qa
Use for:
- finance education
- definitions
- investing concepts
- SIP
- ETF
- mutual funds
- tax basics

2. market_agent
Use for:
- stock prices
- company information
- follow-up market questions
- buy/sell discussions
- company comparisons

3. portfolio_agent
Use for:
- portfolio analysis
- diversification
- allocation
- holdings
- rebalancing
- investment suggestions
     
4. news_agent
Use for:
- latest news
- company news
- stock news
- market news
- financial news
- news summaries
- why a stock moved
- recent market events    

You will receive the complete conversation history.

Use previous messages to understand follow-up questions.

Return ONLY one of:

finance_qa

market_agent

portfolio_agent
     
news_agent     

Do not explain your decision.
Do not answer the user's question.   
"""),

    MessagesPlaceholder(variable_name="messages")

])

router_agent = router_agent_prompt | llm

