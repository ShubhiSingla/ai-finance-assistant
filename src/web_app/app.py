# App - Streamlit entry point; sets up navigation and shared session state
import streamlit as st

st.set_page_config(
    page_title="AI Finance Assistant",
    page_icon="💰",
    layout="wide",
)


def main():
    st.title("💰 AI Finance Assistant")
    st.sidebar.title("Navigation")

    # TODO: configure st.navigation() with pages once Streamlit >=1.36
    st.info("Select a page from the sidebar to get started.")


if __name__ == "__main__":
    main()
