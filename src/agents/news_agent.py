from langchain_openai import ChatOpenAI

from src.tools.news_tools import get_news

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

news_agent = llm.bind_tools(
    [
        get_news
    ]
)

print(get_news.args)