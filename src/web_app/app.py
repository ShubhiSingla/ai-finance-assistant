import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.rag.ingest import load_documents
from src.rag.chunking import split_documents
from src.rag.vector_store import create_vector_store
from src.agents.finance_qa_agent import finance_qa_agent
from src.workflow.graph import build_graph

st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Finance Assistant")

st.write("Ask finance-related questions.")


@st.cache_resource #Streamlit stores the vector DB in memory after first run. Later - user asks new question → reuse same vector store, → much faster
def initialize_vector_store():

    docs = load_documents()

    splits = split_documents(docs)

    vector_store = create_vector_store(splits)

    return vector_store

vector_store = initialize_vector_store()
graph = build_graph()


query = st.chat_input("Ask a finance question...")


if query:

    with st.chat_message("user"):
        st.write(query)

    result = graph.invoke(
    {
        "user_query": query,
        "chat_history": [],
        "response": "",
        "vector_store": vector_store
    }
)

    response = result["response"]

    with st.chat_message("assistant"):
        st.write(response)