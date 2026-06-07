from dotenv import load_dotenv

load_dotenv()

from src.rag.ingest import load_documents
from src.rag.chunking import split_documents
from src.rag.vector_store import create_vector_store
from src.agents.finance_qa_agent import finance_qa_agent


def main():

    docs = load_documents()

    splits = split_documents(docs)

    vector_store = create_vector_store(splits)

    query = "What is diversification?"

    response = finance_qa_agent(
        query,
        vector_store
    )

    print("\nQuestion:")
    print(query)

    print("\nAnswer:")
    print(response)


if __name__ == "__main__":
    main()