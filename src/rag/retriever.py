# Retriever - wraps vector store to fetch relevant document chunks for a query


def get_retriever(vector_store, search_type: str = "similarity", k: int = 5):
    """Build a retriever from a vector store.

    Args:
        vector_store: initialized vector store instance
        search_type: "similarity" or "mmr"
        k: number of top documents to retrieve

    TODO: configure retriever with appropriate search params
    """
    # TODO: return vector_store.as_retriever(search_type=search_type, search_kwargs={"k": k})
    raise NotImplementedError
