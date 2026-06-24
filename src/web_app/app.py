import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.rag.ingest import load_documents
from src.rag.chunking import split_documents
from src.rag.vector_store import create_vector_store
from src.workflow.graph import build_graph
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Finance Assistant")
st.write("Ask me anything about finance, stocks, or your portfolio.")

# --- Vector store & graph (cached so they load only once) ---
@st.cache_resource
def initialize_vector_store():
    docs = load_documents()
    splits = split_documents(docs)
    return create_vector_store(splits)

@st.cache_resource
def initialize_graph():
    return build_graph()

vector_store = initialize_vector_store()
graph = initialize_graph()

# --- Initialize chat history in session state on first load ---
# st.session_state persists across Streamlit reruns within the same session
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Replay all previous messages on every rerun ---
# This is what makes the conversation feel like ChatGPT
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- Chat input ---
query = st.chat_input("Ask a finance question...")

if query:

    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Convert Streamlit messages to LangChain messages
    chat_history = []

    for message in st.session_state.messages:

        if message["role"] == "user":
            chat_history.append(
                HumanMessage(content=message["content"])
            )

        else:
            chat_history.append(
                AIMessage(content=message["content"])
            )    

    # Send query to LangGraph and get response
    with st.spinner("Thinking..."):
        result = graph.invoke(
            {
                "user_query": query,
                "chat_history": chat_history,
                "response": "",
                "vector_store": vector_store
            }
        )

    response = result["response"]

    # Append and display assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)