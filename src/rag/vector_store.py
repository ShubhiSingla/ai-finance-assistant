from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_store(splits):

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large"
    )

    vector_store = FAISS.from_documents(
        documents=splits,
        embedding=embeddings
    )

    return vector_store