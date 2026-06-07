# Helpers - shared utility functions used across the project


def format_currency(amount: float, symbol: str = "$") -> str:
    """Format a float as a currency string. e.g. 1234567.89 → '$1,234,567.89'"""
    return f"{symbol}{amount:,.2f}"


def truncate_text(text: str, max_chars: int = 500) -> str:
    """Truncate text to max_chars, appending ellipsis if trimmed."""
    return text if len(text) <= max_chars else text[:max_chars] + "..."


def flatten_docs(docs: list) -> str:
    """Concatenate a list of LangChain Document objects into a single string."""
    # TODO: return "\n\n".join(doc.page_content for doc in docs)
    raise NotImplementedError
