def build_prompt(query: str, context: str):

    prompt = f"""
    You are an AI Finance Assistant.

    Answer the user's question using ONLY the provided context.

    If the answer is not present in the context,
    say that you do not have enough information.

    Context:
    {context}

    User Question:
    {query}
    """

    return prompt