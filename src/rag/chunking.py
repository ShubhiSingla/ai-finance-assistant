from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )

    splits = text_splitter.split_documents(docs)

    return splits