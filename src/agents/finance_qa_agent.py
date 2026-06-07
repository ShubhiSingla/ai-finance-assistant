from langchain_openai import ChatOpenAI

from src.rag.retriever import retrieve_context
from src.rag.prompt_builder import build_prompt


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


def finance_qa_agent(query: str, vector_store):

    context, retrieved_docs = retrieve_context(
        query,
        vector_store
    )

    prompt = build_prompt(
        query,
        context
    )

    response = llm.invoke(prompt)

    return response.content