# Chat Page - conversational interface routed through the LangGraph workflow
import streamlit as st


def render():
    st.header("💬 Finance Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ask me anything about finance..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # TODO: invoke build_graph().invoke({"query": prompt, ...})
        response = "🚧 Agent response coming soon..."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)


render()
