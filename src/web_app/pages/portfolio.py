# Portfolio Page - displays portfolio holdings, allocation, and AI-driven insights
import streamlit as st


def render():
    st.header("📊 Portfolio Analyzer")

    st.subheader("Upload or Enter Holdings")
    # TODO: add file uploader for CSV or manual entry form
    st.info("Portfolio input UI coming soon.")

    st.subheader("AI Insights")
    # TODO: invoke PortfolioAgent with user holdings
    st.info("Portfolio insights coming soon.")


render()
