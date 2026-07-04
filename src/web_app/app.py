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

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Chat input */
    .stChatInput {
        border-radius: 25px;
    }
    
    /* Title styling */
    h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle */
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: transform 0.2s;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("💰 AI Finance Assistant")
st.markdown('<p class="subtitle">Your intelligent companion for finance, stocks, and investment guidance</p>', unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 🤖 About")
    st.markdown("""
    Multi-agent AI assistant powered by:
    - **LangGraph** for orchestration
    - **OpenAI GPT-4o** for intelligence
    - **RAG** for grounded answers
    - **Yahoo Finance** for live data
    - **NewsAPI** for financial news
    """)
    
    st.markdown("---")
    
    st.markdown("### 💡 Capabilities")
    st.markdown("""
    - 📚 Finance education & concepts
    - 📈 Live stock prices
    - 💼 Portfolio analysis
    - 📰 Financial news summaries
    - 💬 Context-aware conversations
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Session Stats")
    message_count = len(st.session_state.get("messages", []))
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", message_count)
    with col2:
        user_messages = len([m for m in st.session_state.get("messages", []) if m["role"] == "user"])
        st.metric("Queries", user_messages)
    
    st.markdown("---")
    
    if st.button("🔄 Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("<small>Built with ❤️ using LangGraph & Streamlit</small>", unsafe_allow_html=True)

# --- Vector store & graph (cached so they load only once) ---
@st.cache_resource
def initialize_vector_store():
    docs = load_documents()
    splits = split_documents(docs)
    return create_vector_store(splits)

@st.cache_resource
def initialize_graph():
    return build_graph()

with st.spinner("🚀 Initializing AI systems..."):
    vector_store = initialize_vector_store()
    graph = initialize_graph()

# --- Initialize chat history in session state on first load ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Welcome message ---
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown("""
        👋 Welcome! I'm your AI Finance Assistant.
        
        **Ask me about:**
        - 📚 Financial concepts (e.g., "What is SIP?")
        - 📈 Stock prices (e.g., "What's Apple's stock price?")
        - 💼 Portfolio analysis (e.g., "Analyze my portfolio")
        - 📰 Market news (e.g., "Latest Tesla news")
        
        I maintain conversation context, so feel free to ask follow-up questions!
        """)

# --- Replay all previous messages on every rerun ---
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# --- Chat input ---
query = st.chat_input("💬 Ask me anything about finance, stocks, or investments...")

if query:
    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user", avatar="👤"):
        st.markdown(query)

    # Convert Streamlit messages to LangChain messages
    chat_history = []
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_history.append(HumanMessage(content=message["content"]))
        else:
            chat_history.append(AIMessage(content=message["content"]))

    # Send query to LangGraph and get response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🧠 Analyzing your question..."):
            result = graph.invoke(
                {
                    "user_query": query,
                    "chat_history": chat_history,
                    "response": "",
                    "vector_store": vector_store
                }
            )
        
        response = result["response"]
        st.markdown(response)
        
        # Append assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})