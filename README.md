# 💰 AI Finance Assistant

AI Finance Assistant is a modular, multi-agent financial assistant built using **LangGraph**, **LangChain**, **OpenAI**, **FAISS**, **Retrieval-Augmented Generation (RAG)**, **Yahoo Finance**, and **Streamlit**.

The assistant helps users learn financial concepts, retrieve live stock prices, and analyze investment portfolios through specialized AI agents. Instead of using a single large prompt for every request, the application uses a LangGraph-based multi-agent architecture, where an LLM Router intelligently selects the most suitable agent based on the user's query and conversation history.

---

## ✨ Features

- 📚 Finance Question Answering using Retrieval-Augmented Generation (RAG)
- 📈 Live Stock Price Retrieval using Yahoo Finance
- 💼 AI-powered Portfolio Analysis and Investment Suggestions
- 🤖 Multi-Agent Architecture using LangGraph
- 🧠 LLM-based Intelligent Query Routing
- 🛠️ Tool Calling with LangChain
- 💬 Conversational Chat Interface built with Streamlit
- 💾 Session-based Conversation History
- 📰 Financial News Retrieval and Summarization
- ⚠️ Graceful Error Handling for External APIs

---

## Architecture

```text
                              User
                                │
                                ▼
                     Streamlit Chat Interface
                                │
                                ▼
         Session-based Conversation History
          (st.session_state.messages)
                                │
                                ▼
                    LangGraph Workflow
                  (FinanceAgentState)
                                │
                                ▼
                       LLM Router Agent
      (Understands the user's intent using conversation history)
                                │
        ┌───────────────────────┼──────────────────────┬────────────────────────┐
        ▼                       ▼                      ▼                        ▼
 Finance QA Agent        Market Agent         Portfolio Agent             News Agent
        │                       │                      │                        │
        ▼                       ▼                      ▼               ┌────────┴────────┐
   RAG Pipeline         Yahoo Finance Tool  Portfolio Analysis Tool    ▼                 ▼
        │                       │                      │         Yahoo Finance        NewsAPI
        ▼                       ▼                      ▼           News Tool           Tool
 FAISS Retriever      Live Stock Prices    Portfolio Analytics          │                 │
        │                       │                      │               └────────┬────────┘
        └───────────────────────┼──────────────────────┘                        │
                                └────────────────────────────────────────────────┘
                                ▼
                     OpenAI Language Models
                                │
                                ▼
                        Final AI Response
                                │
                                ▼
                     Streamlit Chat Interface
```

---

## Project Structure

```text
ai_finance_assistant/

├── src/
│
├── agents/
│   ├── finance_qa_agent.py
│   ├── market_agent.py
│   ├── portfolio_agent.py
│   ├── news_agent.py
│   └── router_agent.py
│
├── rag/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   └── vector_store.py
│
├── workflow/
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── tools/
│   ├── market_data.py
│   ├── portfolio_tools.py
│   ├── news_tools.py
│   └── yahoo_news.py
│
├── web_app/
│   └── app.py
│
├── data/
│
├── tests/
│
├── requirements.txt
└── README.md
```

| Folder | Description |
|----------|-------------|
| `agents/` | Contains all AI agents: Finance QA, Market, Portfolio, and LLM Router. |
| `rag/` | Implements the complete RAG pipeline including document ingestion, chunking, embeddings, retrieval, and prompt generation. |
| `workflow/` | Defines the LangGraph workflow including state management, nodes, routing, and graph orchestration. |
| `tools/` | Contains LangChain tools for live stock price retrieval, portfolio analysis, and financial news retrieval. |
| `web_app/` | Streamlit-based conversational web application. |
| `data/` | Stores documents and vector database files used by the RAG pipeline. |
| `tests/` | Unit tests for tools, agents, router, and LangGraph workflow. |

---

## Specialized AI Agents

The AI Finance Assistant follows a multi-agent architecture where each agent is responsible for a specific task. An LLM-based Router Agent analyzes the user's query and conversation history, then forwards the request to the most appropriate specialized agent.

---

### 1. Finance QA Agent

Answers finance-related educational questions using a RAG pipeline. Instead of relying only on the LLM's pre-trained knowledge, it retrieves relevant information from a financial knowledge base before generating a grounded response.

**Technologies:** LangChain · OpenAI GPT-4.1-mini · OpenAI Embeddings · FAISS · WebBaseLoader · Investopedia Knowledge Base

**Workflow:**
```text
User Question → Retrieve Relevant Documents (FAISS) → Build Prompt → GPT-4.1-mini → Grounded Response
```

**Example Questions:**
```
What is SIP?
Explain Mutual Funds.
What is an ETF?
Difference between SIP and Lump Sum.
```

---

### 2. Market Agent

Retrieves live stock market information using Yahoo Finance. Uses LangChain Tool Calling to identify when a tool is required, fetches live market data, and generates a natural language response.

**Technologies:** LangChain Tool Calling · OpenAI GPT-4o · Yahoo Finance (yfinance)

**Workflow:**
```text
User Question → GPT-4o → Tool Call → Yahoo Finance → Tool Result → ToolMessage → GPT-4o → Final Response
```

**Example Questions:**
```
What is Apple's stock price?
What is Tesla's current stock price?
Should I buy Apple stock?
```

---

### 3. Portfolio Agent

Analyzes a user's investment portfolio and provides insights into allocation, diversification, concentration risk, and improvement suggestions. Uses a custom portfolio analysis tool with OpenAI Tool Calling.

**Technologies:** LangChain Tool Calling · OpenAI GPT-4o · Custom Portfolio Analysis Tool

**Workflow:**
```text
User Portfolio → GPT-4o → Tool Call → Portfolio Analysis Tool → Tool Result → ToolMessage → GPT-4o → Portfolio Insights
```

**Example Questions:**
```
Analyze my portfolio.
Is my portfolio diversified?
How risky is my portfolio?
How can I reduce the risk?
```

**Capabilities:**
- Calculate total portfolio value and asset allocation percentages
- Analyze portfolio diversification and detect concentration risk
- Identify portfolio strengths and areas for improvement
- Provide investment suggestions and rebalancing recommendations

---

### 4. News Agent

Retrieves and summarizes financial news from multiple sources. Uses LangChain Tool Calling to automatically select between Yahoo Finance News and NewsAPI depending on the nature of the query — Yahoo Finance for company-specific news and NewsAPI for broader financial topics such as inflation, interest rates, Federal Reserve announcements, and general market news. The LLM generates a concise summary of the retrieved articles.

**Technologies:** LangChain Tool Calling · OpenAI GPT-4o · Yahoo Finance News · NewsAPI

**Workflow:**
```text
User Question → GPT-4o → Tool Selection → Yahoo Finance News Tool / NewsAPI Tool → Tool Result → ToolMessage → GPT-4o → News Summary
```

**Example Questions:**
```
Latest Apple news.
Latest Tesla news.
Latest Federal Reserve news.
Latest inflation news.
Summarize today's AI market news.
```

---

### 5. LLM Router Agent

Selects the most appropriate specialized agent for every user request. Analyzes both the current user query and the complete conversation history to make a context-aware routing decision — enabling correct handling of follow-up questions without keyword matching.

**Technologies:** LangGraph · LangChain · OpenAI GPT-4.1-mini

**Routes:**
- `finance_qa` — Finance concepts, definitions, educational questions
- `market_agent` — Live stock prices, market data, trading decisions
- `portfolio_agent` — Portfolio analysis, diversification, risk assessment
- `news_agent` — Financial news retrieval, company news, market news, macro topics

**Multi-turn Example:**
```
User: What is Apple's current stock price?   → Market Agent
User: Should I buy it?                       → Market Agent ✅ (understands "it" = Apple)

User: Analyze my portfolio.                  → Portfolio Agent
User: How can I reduce the risk?             → Portfolio Agent ✅ (understands prior context)

User: Latest news on Tesla.                  → News Agent
User: How has it affected the stock?         → News Agent ✅ (understands prior context)
```

---

## LangGraph Workflow

The AI Finance Assistant uses **LangGraph** to orchestrate multiple specialized AI agents. Every user request flows through a centralized workflow where the Router Agent first determines which specialized agent should handle the request.

The workflow is coordinated using **FinanceAgentState**, which stores the current user query, conversation history, vector store, router decision, and final response. Each node in the graph performs a single responsibility, making the application modular, easy to maintain, and straightforward to extend.

```text
User Query → Update Conversation History → FinanceAgentState → LLM Router Agent
    │
    ├──→ Finance QA Agent → RAG Pipeline
    ├──→ Market Agent → Yahoo Finance Tool
    ├──→ Portfolio Agent → Portfolio Tool
    └──→ News Agent → Yahoo Finance News Tool / NewsAPI Tool
    │
    └──→ Generate Response → Return to Streamlit
```

---

## RAG Pipeline

The Finance QA Agent uses a RAG pipeline to answer finance-related questions by retrieving relevant information from a financial knowledge base before generating a response.

```text
Financial Documents (Investopedia)
    → WebBaseLoader
    → RecursiveCharacterTextSplitter
    → OpenAI Embeddings (text-embedding-3-large)
    → FAISS Vector Store
    → Similarity Search Retriever
    → Prompt Builder
    → GPT-4.1-mini
    → Grounded Response
```

---

## Tool Calling Workflow

The Market Agent, Portfolio Agent, and News Agent use **LangChain Tool Calling** to interact with external tools. The LLM determines whether a tool is required, generates a structured tool call, executes it, and uses the result to produce a natural language response.

```text
User Query → LLM → Tool Call? ──Yes──→ Execute Tool → ToolMessage → LLM → Final Response
                         └──No──→ Generate Response directly
```

---

## Implemented Features

### RAG
- ✅ Financial document ingestion, chunking, embeddings, FAISS vector store, semantic search, prompt construction, grounded response generation

### Finance QA Agent
- ✅ RAG-powered Q&A · Context-aware prompts · Finance knowledge base integration

### Market Agent
- ✅ Tool calling · Yahoo Finance integration · Live stock & company data · Multi-turn conversations · Graceful error handling

### Portfolio Agent
- ✅ Portfolio analysis tool · Value & allocation calculation · Diversification & concentration risk analysis · Investment suggestions

### News Agent
- ✅ Multi-tool agent · Yahoo Finance News · NewsAPI integration · Automatic tool selection · Financial news summarization · Company-specific news · Market news · Graceful error handling

### LLM Router
- ✅ Conversation-aware routing · Multi-turn query understanding · Dynamic agent selection via GPT-4.1-mini

### LangGraph Workflow
- ✅ FinanceAgentState · Router, QA, Market, Portfolio, and News nodes · Conditional routing · Multi-agent orchestration

### Streamlit Application
- ✅ Conversational chat interface · Session-based history · Cached vector store & workflow

### Testing
- ✅ Workflow · Router · Market tool · Portfolio tool · Portfolio agent tests

---

## Example Queries

**News:** `Latest Apple news.` · `Latest Tesla news.` · `Latest Federal Reserve news.` · `Latest inflation news.` · `Summarize today's AI market news.`

**Finance QA:** `What is SIP?` · `Explain Mutual Funds.` · `What is an ETF?` · `Difference between ETF and Mutual Fund.`

**Market:** `What is Apple's current stock price?` · `Compare Apple and NVIDIA.` · `Should I buy Apple stock?`

**Portfolio:** `Analyze my portfolio.` · `Is my portfolio diversified?` · `How can I reduce the risk?`

**Example Portfolio Input:**
```
Apple  — 10 shares @ $290
Tesla  — 5 shares  @ $320
NVIDIA — 8 shares  @ $170
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangGraph | Multi-agent workflow orchestration |
| LangChain | LLM integration and Tool Calling |
| OpenAI GPT-4.1-mini | Finance QA Agent & LLM Router |
| OpenAI GPT-4o | Market Agent & Portfolio Agent |
| OpenAI Embeddings (`text-embedding-3-large`) | Vector Embeddings |
| FAISS | Vector Database |
| Yahoo Finance (yfinance) | Live Market Data |
| NewsAPI | Financial News Retrieval |
| Streamlit | Web Application |
| BeautifulSoup | Document Parsing |
| Pytest | Unit Testing |

---

## Roadmap

### Conversational AI
- [x] Session-based Chat History · Multi-turn Conversations
- [ ] Persistent User Memory · Cross-session Memory · Source Citations

### Agents
- [x] Finance QA · Market · Portfolio · LLM Router · Financial News
- [ ] Goal Planner · Tax · Compliance

### Market Intelligence
- [x] Live Stock Prices
- [ ] Historical Prices · ETF Analysis · Company Fundamentals · Financial Ratios · Earnings Analysis

### Portfolio
- [x] Portfolio Analysis · Diversification Analysis
- [ ] Risk Score · Portfolio Optimization · Sector Analysis

### Production
- [ ] Pydantic Tool Schemas · Docker · CI/CD Pipeline · Logging & Monitoring · Cloud Deployment

---

## Getting Started

```bash
# Clone the repository
git clone <repository-url>
cd ai_finance_assistant

# Create and activate a virtual environment
python -m venv .venv

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
echo "OPENAI_API_KEY=your_api_key" > .env

# Run the application
streamlit run src/web_app/app.py
```

---

## Future Enhancements

- Personalized & Goal-Based Financial Planning
- News Sentiment Analysis
- AI-powered Market Impact Analysis
- Personalized Financial News Feed
- Company Watchlist Alerts
- News-to-Portfolio Impact Analysis
- Voice Assistant
- MCP Integration
- Broker Account Integration (e.g., Zerodha)
- Portfolio Import
- Advanced Financial Analytics

---

## Author

**Shubhi Singla**

AI Finance Assistant is a personal engineering project built to explore modern AI application development using LangGraph, LangChain, Retrieval-Augmented Generation (RAG), Tool Calling, and Multi-Agent Architectures. The project demonstrates how specialized AI agents can collaborate to solve real-world financial tasks through intelligent routing, external tools, and modular workflows.