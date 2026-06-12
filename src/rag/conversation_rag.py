from langchain_openai import ChatOpenAI

from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)

from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


def build_conversational_rag_chain(vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    # Query rewriting prompt
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Given chat history and latest user question, "
                "rewrite the question into a standalone question.",
            ),

            MessagesPlaceholder("chat_history"),

            ("human", "{input}"),
        ]
    )

    history_aware_retriever = create_history_aware_retriever(
        llm,
        retriever,
        contextualize_q_prompt,
    )

    # QA prompt
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are an AI Finance Assistant.

                Answer the question using ONLY the provided context.

                If answer is not available in context,
                say you do not have enough information.
                Write the answer in easy English. 
                If required, make pointers.

                Context:
                {context}
                """
            ),

            MessagesPlaceholder("chat_history"),

            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(
        llm,
        qa_prompt
    )

    rag_chain = create_retrieval_chain(
        history_aware_retriever,
        question_answer_chain
    )

    return rag_chain