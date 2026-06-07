# Market Page - displays live market data, charts, and AI-generated summaries
import streamlit as st


def render():
    st.header("📈 Market Overview")

    ticker = st.text_input("Enter ticker symbol (e.g. AAPL, TSLA):", "AAPL")

    if st.button("Fetch Data"):
        # TODO: invoke get_stock_price(ticker) and get_historical_data(ticker)
        st.info(f"Market data for {ticker} coming soon.")


render()
