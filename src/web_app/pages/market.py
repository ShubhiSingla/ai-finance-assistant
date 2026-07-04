# Market Page - displays live market data and AI-generated summaries
import streamlit as st
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.tools.market_data import get_stock_price
from src.agents.market_agent import market_agent
from langchain_core.messages import HumanMessage, ToolMessage

# --- Custom CSS ---
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 3rem;
        font-size: 1.1rem;
        font-weight: 700;
        transition: all 0.3s;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }
    
    .stock-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def render():
    # --- Header ---
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem;'>📈 Live Market Data</h1>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.3rem;'>Get real-time stock prices and AI-powered insights</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Popular tickers quick access ---
    st.markdown("### 🔥 Popular Stocks")
    popular_tickers = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "NFLX"]
    cols = st.columns(len(popular_tickers))
    
    selected_ticker = None
    for idx, ticker in enumerate(popular_tickers):
        with cols[idx]:
            if st.button(ticker, key=f"btn_{ticker}"):
                selected_ticker = ticker
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- Manual ticker input ---
    col1, col2 = st.columns([3, 1])
    with col1:
        ticker_input = st.text_input(
            "🔍 Enter Stock Ticker or Company Name",
            value=selected_ticker if selected_ticker else "AAPL",
            placeholder="e.g., AAPL, Apple, Tesla, Microsoft"
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        fetch_button = st.button("🚀 Get Stock Data", use_container_width=True)

    if fetch_button or selected_ticker:
        ticker = ticker_input.upper()
        
        with st.spinner(f"📊 Fetching data for {ticker}..."):
            # Fetch stock price using the tool
            result = get_stock_price.invoke({"ticker": ticker})
            
            if result["status"] == "error":
                st.error(f"❌ {result['message']}")
                return
            
            # Display stock data
            st.markdown(f"""
            <div class='stock-card'>
                <h2 style='color: #667eea; margin-bottom: 1rem;'>{result['company']} ({result['ticker']})</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Key metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "💰 Current Price",
                    f"{result['currency']} {result['current_price']:,.2f}"
                )
            
            with col2:
                st.metric(
                    "🏢 Company",
                    result['company']
                )
            
            with col3:
                st.metric(
                    "🎫 Ticker",
                    result['ticker']
                )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # AI Analysis section
            st.markdown("### 🤖 AI Market Analysis")
            
            with st.spinner("🧠 Generating AI insights..."):
                # Use Market Agent to generate insights
                query = f"Provide a brief analysis of {ticker} stock at current price of {result['current_price']} {result['currency']}"
                
                response = market_agent.invoke({
                    "messages": [HumanMessage(content=query)]
                })
                
                if response.tool_calls:
                    # Agent wants to call a tool (shouldn't happen since we already have data)
                    tool_call = response.tool_calls[0]
                    tool_result = get_stock_price.invoke(tool_call["args"])
                    
                    tool_message = ToolMessage(
                        content=str(tool_result),
                        tool_call_id=tool_call["id"]
                    )
                    
                    final_response = market_agent.invoke({
                        "messages": [
                            HumanMessage(content=query),
                            response,
                            tool_message
                        ]
                    })
                    
                    ai_analysis = final_response.content
                else:
                    ai_analysis = response.content
                
                st.info(ai_analysis)
            
            # Additional actions
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📰 Want More?")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"📰 Get {ticker} News", use_container_width=True):
                    with st.spinner(f"📰 Fetching latest news for {ticker}..."):
                        from src.agents.news_agent import news_agent
                        from src.tools.yahoo_news import get_company_news
                        from src.tools.news_tools import fetch_news
                        
                        try:
                            # Call news agent
                            news_query = f"Latest {ticker} news"
                            news_response = news_agent.invoke({
                                "messages": [HumanMessage(content=news_query)]
                            })
                            
                            if news_response.tool_calls:
                                tool_call = news_response.tool_calls[0]
                                tool_name = tool_call["name"]
                                
                                # Route to correct tool
                                if tool_name == "get_company_news":
                                    tool_result = get_company_news.invoke(tool_call["args"])
                                else:
                                    tool_result = fetch_news.invoke(tool_call["args"])
                                
                                # Check for errors
                                if isinstance(tool_result, list) and len(tool_result) > 0:
                                    if tool_result[0].get("status") == "error":
                                        st.warning(f"⚠️ {tool_result[0]['message']}")
                                    else:
                                        # Pass result to agent for summary
                                        tool_message = ToolMessage(
                                            content=str(tool_result),
                                            tool_call_id=tool_call["id"]
                                        )
                                        
                                        final_news_response = news_agent.invoke({
                                            "messages": [
                                                HumanMessage(content=news_query),
                                                news_response,
                                                tool_message
                                            ]
                                        })
                                        
                                        st.success("📰 Latest News")
                                        st.markdown(final_news_response.content)
                                else:
                                    st.warning(f"⚠️ No news articles found for {ticker}")
                            else:
                                st.markdown(news_response.content)
                        
                        except Exception as e:
                            st.error(f"❌ Error fetching news: {str(e)}")
            
            with col2:
                if st.button(f"📊 Add {ticker} to Portfolio", use_container_width=True):
                    st.info("Portfolio tracking feature coming soon!")


render()
