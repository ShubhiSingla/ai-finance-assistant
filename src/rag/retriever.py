def retrieve_context(query: str, vector_store):

    retrieved_docs = vector_store.similarity_search(
        query,
        k=2
    )

    serialized = "\n\n".join(
        (
            f"Source: {doc.metadata}\n"
            f"Content: {doc.page_content}"
        )
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs