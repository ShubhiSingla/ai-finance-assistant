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
- ⚠️ Graceful Error Handling for External APIs

---

# Architecture

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
        ┌───────────────────────┼────────────────────────┐
        ▼                       ▼                        ▼
 Finance QA Agent        Market Agent         Portfolio Agent
        │                       │                        │
        ▼                       ▼                        ▼
   RAG Pipeline         Yahoo Finance Tool     Portfolio Analysis Tool
        │                       │                        │
        ▼                       ▼                        ▼
 FAISS Retriever      Live Stock Prices      Portfolio Analytics
        │                       │                        │
        └───────────────────────┼────────────────────────┘
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

# Project Structure

```text
ai_finance_assistant/

├── src/
│
├── agents/
│   ├── finance_qa_agent.py
│   ├── market_agent.py
│   ├── portfolio_agent.py
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
│   └── portfolio_tools.py
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

## Folder Description

| Folder | Description |
|----------|-------------|
| `agents/` | Contains all AI agents such as Finance QA, Market, Portfolio, and LLM Router Agent. |
| `rag/` | Implements the complete Retrieval-Augmented Generation (RAG) pipeline including document ingestion, chunking, embeddings, retrieval, and prompt generation. |
| `workflow/` | Defines the LangGraph workflow including state management, nodes, routing, and graph orchestration. |
| `tools/` | Contains LangChain tools used by AI agents, such as live stock price retrieval and portfolio analysis. |
| `web_app/` | Streamlit-based conversational web application. |
| `data/` | Stores documents and vector database files used by the RAG pipeline. |
| `tests/` | Unit tests for tools, agents, router, and LangGraph workflow. |

---

# Specialized AI Agents

The AI Finance Assistant follows a multi-agent architecture where each agent is responsible for a specific task. An LLM-based Router Agent analyzes the user's query and conversation history, then forwards the request to the most appropriate specialized agent.

---

## 1. Finance QA Agent

### Purpose

The Finance QA Agent answers finance-related educational questions using a Retrieval-Augmented Generation (RAG) pipeline. Instead of relying only on the LLM's pre-trained knowledge, it retrieves relevant information from a financial knowledge base before generating a grounded response.

### Workflow

```text
User Question
      │
      ▼
Retrieve Relevant Documents (FAISS)
      │
      ▼
Build Prompt
      │
      ▼
OpenAI GPT-4.1-mini
      │
      ▼
Grounded Response
```

### Technologies Used

- LangChain
- OpenAI GPT-4.1-mini
- OpenAI Embeddings
- FAISS
- WebBaseLoader
- Investopedia Knowledge Base

### Example Questions

```text
What is SIP?

Explain Mutual Funds.

What is an ETF?

Difference between SIP and Lump Sum.
```

---

## 2. Market Agent

### Purpose

The Market Agent retrieves live stock market information using Yahoo Finance. It uses LangChain Tool Calling to identify when a tool is required, fetches live market data, and then generates a natural language response for the user.

### Workflow

```text
User Question
      │
      ▼
OpenAI GPT-4o
      │
      ▼
Tool Call
      │
      ▼
Yahoo Finance Tool
      │
      ▼
Tool Result
      │
      ▼
ToolMessage
      │
      ▼
OpenAI GPT-4o
      │
      ▼
Final Response
```

### Technologies Used

- LangChain Tool Calling
- OpenAI GPT-4o
- Yahoo Finance (yfinance)

### Example Questions

```text
What is Apple's stock price?

What is Tesla's current stock price?

Should I buy Apple stock?
```

---

## 3. Portfolio Agent

### Purpose

The Portfolio Agent analyzes a user's investment portfolio and provides insights into portfolio allocation, diversification, concentration risk, and possible improvements. It uses a custom portfolio analysis tool together with OpenAI Tool Calling.

### Workflow

```text
User Portfolio
      │
      ▼
OpenAI GPT-4o
      │
      ▼
Tool Call
      │
      ▼
Portfolio Analysis Tool
      │
      ▼
Tool Result
      │
      ▼
ToolMessage
      │
      ▼
OpenAI GPT-4o
      │
      ▼
Portfolio Insights
```

### Technologies Used

- LangChain Tool Calling
- OpenAI GPT-4o
- Custom Portfolio Analysis Tool

### Example Questions

```text
Analyze my portfolio.

Is my portfolio diversified?

How risky is my portfolio?

How can I reduce the risk?
```

### Current Capabilities

- Calculate total portfolio value
- Calculate asset allocation percentages
- Analyze portfolio diversification
- Detect concentration risk
- Identify portfolio strengths
- Highlight areas for improvement
- Provide investment suggestions and rebalancing recommendations

## 4. LLM Router Agent

### Purpose

The LLM Router Agent is responsible for selecting the most appropriate specialized agent for every user request. Instead of relying on keyword matching, it analyzes both the current user query and the complete conversation history before making a routing decision.

### Workflow

Conversation History
        │
        ▼
Current User Query
        │
        ▼
OpenAI GPT-4.1-mini
        │
        ▼
Route Selection
        │
        ├───────────────┬────────────────┐
        ▼               ▼                ▼
finance_qa       market_agent     portfolio_agent

### Technologies Used

- LangGraph
- LangChain
- OpenAI GPT-4.1-mini

### Current Capabilities

- Intent Classification
- Conversation-aware Routing
- Multi-turn Follow-up Support
- Dynamic Agent Selection

---

# LangGraph Workflow

The AI Finance Assistant uses **LangGraph** to orchestrate multiple specialized AI agents. Every user request flows through a centralized workflow where the Router Agent first determines which specialized agent should handle the request.

```text
                         User Query
                              │
                              ▼
                Update Conversation History
                              │
                              ▼
                FinanceAgentState (LangGraph)
                              │
                              ▼
                     LLM Router Agent
          (Analyzes the complete conversation)
                              │
      ┌───────────────────────┼───────────────────────┐
      ▼                       ▼                       ▼
Finance QA Agent       Market Agent         Portfolio Agent
      │                       │                       │
      ▼                       ▼                       ▼
 RAG Pipeline         Yahoo Finance Tool     Portfolio Tool
      │                       │                       │
      └───────────────────────┼───────────────────────┘
                              ▼
                      Generate Response
                              │
                              ▼
                     Return to Streamlit
```

The workflow is coordinated using **FinanceAgentState**, which stores the current user query, conversation history, vector store, router decision, and final response. Each node in the graph performs a single responsibility, making the application modular, easy to maintain, and straightforward to extend with additional agents in the future.

---

# LLM Router Agent

The AI Finance Assistant uses an **LLM-based Router Agent** to determine which specialized agent should answer a user's request.

Unlike a traditional keyword-based router, the Router Agent analyzes the **complete conversation history** along with the current user query. This enables the assistant to correctly understand conversational follow-up questions and route them to the appropriate agent.

---

## Routing Workflow

```text
Conversation History
        │
        ▼
Current User Query
        │
        ▼
OpenAI GPT-4.1-mini
        │
        ▼
Classify Request
        │
        ├───────────────┬────────────────┐
        ▼               ▼                ▼
finance_qa       market_agent     portfolio_agent
```

The Router Agent returns only one of the following routes:

- `finance_qa`
- `market_agent`
- `portfolio_agent`

LangGraph then forwards the request to the selected agent.

---

## Example Routing

### Finance Questions

```text
What is SIP?

Explain Mutual Funds.

Difference between ETF and Mutual Fund.
```

↓

Finance QA Agent

---

### Market Questions

```text
What is Apple's current stock price?

Should I buy Apple stock?

Compare Apple and Tesla.
```

↓

Market Agent

---

### Portfolio Questions

```text
Analyze my portfolio.

Is my portfolio diversified?

How can I reduce the risk?
```

↓

Portfolio Agent

---

## Multi-turn Conversation Support

One of the biggest advantages of using an LLM Router is its ability to understand follow-up questions.

Example:

```text
User:
What is Apple's current stock price?

↓

Market Agent

User:
Should I buy it?

↓

Market Agent ✅
```

The Router understands that **"it" refers to Apple stock**, even though the company name is not mentioned in the second question.

Similarly,

```text
User:
Analyze my portfolio.

↓

Portfolio Agent

User:
How can I reduce the risk?

↓

Portfolio Agent ✅
```

The Router understands that the follow-up question refers to the previously analyzed portfolio.

This conversational routing significantly improves the user experience compared to a traditional keyword-based router.
---

# RAG Pipeline

The **Finance QA Agent** uses a Retrieval-Augmented Generation (RAG) pipeline to answer finance-related questions. Instead of relying solely on the LLM's pre-trained knowledge, the agent first retrieves relevant information from a financial knowledge base and then uses that context to generate a grounded response.

## Workflow

```text
Financial Documents
(Investopedia Articles)
        │
        ▼
WebBaseLoader
        │
        ▼
Recursive Character Text Splitter
        │
        ▼
OpenAI Embeddings
(text-embedding-3-large)
        │
        ▼
FAISS Vector Store
        │
        ▼
Similarity Search Retriever
        │
        ▼
Relevant Context
        │
        ▼
Prompt Builder
        │
        ▼
OpenAI GPT-4.1-mini
        │
        ▼
Grounded Response
```

### Technologies Used

- WebBaseLoader
- RecursiveCharacterTextSplitter
- OpenAI Embeddings (`text-embedding-3-large`)
- FAISS Vector Store
- Similarity Search Retriever
- OpenAI GPT-4.1-mini

### How It Works

1. Financial articles are loaded from trusted sources using **WebBaseLoader**.
2. The documents are split into smaller chunks using **RecursiveCharacterTextSplitter**.
3. Each chunk is converted into vector embeddings using **OpenAI Embeddings**.
4. The embeddings are stored in a **FAISS Vector Store** for efficient similarity search.
5. When a user asks a finance-related question, the retriever finds the most relevant document chunks.
6. The retrieved context is combined with the user's question to build a grounded prompt.
7. **GPT-4.1-mini** generates the final response using both the retrieved context and the user's query.
```

---

# Tool Calling Workflow

The **Market Agent** and **Portfolio Agent** use **LangChain Tool Calling** to interact with external tools. Instead of generating answers directly, the LLM first determines whether a tool is required. If a tool is needed, it generates a structured tool call, executes the tool, receives the result, and then uses that result to generate a natural language response.

```text
                 User Query
                      │
                      ▼
              OpenAI Language Model
                      │
          Does a tool need to be called?
                      │
                Yes ──┴── No
                 │          │
                 ▼          ▼
          Generate Tool Call   Generate Response
                 │
                 ▼
           Execute Tool
                 │
                 ▼
           Receive Tool Result
                 │
                 ▼
          Create ToolMessage
                 │
                 ▼
      OpenAI Language Model
                 │
                 ▼
          Final AI Response
```

### Market Agent

The Market Agent uses the **Yahoo Finance Tool** to retrieve real-time stock market information.

Example:

```text
User:
What is Apple's current stock price?

↓

OpenAI generates a tool call

↓

get_stock_price("AAPL")

↓

Yahoo Finance returns live stock data

↓

The result is converted into a ToolMessage

↓

OpenAI generates the final response
```

---

### Portfolio Agent

The Portfolio Agent uses a **custom portfolio analysis tool** to calculate investment metrics before generating recommendations.

Example:

```text
User:
Analyze my portfolio

↓

OpenAI generates a tool call

↓

analyze_portfolio(...)

↓

Portfolio metrics are calculated

↓

The result is converted into a ToolMessage

↓

OpenAI generates portfolio insights and recommendations
```

---

# Implemented Features

## Retrieval-Augmented Generation (RAG)

- ✅ Financial document ingestion using WebBaseLoader
- ✅ Recursive document chunking
- ✅ OpenAI Embeddings (`text-embedding-3-large`)
- ✅ FAISS Vector Database
- ✅ Semantic Similarity Search
- ✅ Context Retrieval
- ✅ Prompt Construction
- ✅ Grounded Response Generation

---

## Finance QA Agent

- ✅ RAG-powered Finance Question Answering
- ✅ Context-aware Prompt Generation
- ✅ Grounded Responses
- ✅ Finance Knowledge Base Integration

---

## Market Agent

- ✅ OpenAI Tool Calling
- ✅ Yahoo Finance Integration
- ✅ Live Stock Price Retrieval
- ✅ Company Information Retrieval
- ✅ Multi-turn Market Conversations
- ✅ Graceful API Error Handling

---

## Portfolio Agent

- ✅ Portfolio Analysis Tool
- ✅ Portfolio Value Calculation
- ✅ Asset Allocation Analysis
- ✅ Diversification Analysis
- ✅ Concentration Risk Detection
- ✅ Investment Suggestions
- ✅ Tool Calling Workflow

---

## LLM Router

- ✅ Conversation-aware Routing
- ✅ Multi-turn Query Understanding
- ✅ Intelligent Agent Selection
- ✅ Dynamic Routing using GPT-4.1-mini

---

## LangGraph Workflow

- ✅ FinanceAgentState
- ✅ LLM Router Node
- ✅ Finance QA Node
- ✅ Market Agent Node
- ✅ Portfolio Agent Node
- ✅ Conditional Routing
- ✅ Multi-Agent Orchestration

---

## Streamlit Application

- ✅ Conversational Chat Interface
- ✅ Session-based Chat History
- ✅ Cached Vector Store
- ✅ Cached LangGraph Workflow
- ✅ Interactive User Experience

---

## Testing

- ✅ LangGraph Workflow Tests
- ✅ Router Tests
- ✅ Market Tool Tests
- ✅ Portfolio Tool Tests
- ✅ Portfolio Agent Tests

---

# Example Queries

## Finance QA Agent

```text
What is SIP?

Explain Mutual Funds.

What is an ETF?

Difference between ETF and Mutual Fund.
```

---

## Market Agent

```text
What is Apple's current stock price?

What is Tesla's current stock price?

Compare Apple and NVIDIA.

Should I buy Apple stock?
```

---

## Portfolio Agent

```text
Analyze my portfolio.

Is my portfolio diversified?

How risky is my portfolio?

How can I reduce the risk?
```

Example Portfolio

```text
Apple
10 shares
Price: 290

Tesla
5 shares
Price: 320

NVIDIA
8 shares
Price: 170
```

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangGraph | Multi-agent workflow orchestration |
| LangChain | LLM integration and Tool Calling |
| OpenAI GPT-4.1-mini | Finance QA Agent & LLM Router |
| OpenAI GPT-4o | Market Agent & Portfolio Agent |
| OpenAI Embeddings | Vector Embeddings |
| FAISS | Vector Database |
| Yahoo Finance (yfinance) | Live Market Data |
| Streamlit | Web Application |
| BeautifulSoup | Document Parsing |
| Pytest | Unit Testing |

---

# Roadmap

## Conversational AI

- [x] Session-based Chat History
- [x] Multi-turn Conversations
- [ ] Persistent User Memory
- [ ] Cross-session Memory
- [ ] Source Citations

---

## Agents

- [x] Finance QA Agent
- [x] Market Agent
- [x] Portfolio Agent
- [x] LLM Router Agent
- [ ] Goal Planner Agent
- [ ] Financial News Agent
- [ ] Tax Agent
- [ ] Compliance Agent

---

## Market Intelligence

- [x] Live Stock Prices
- [ ] Historical Stock Prices
- [ ] ETF Analysis
- [ ] Company Fundamentals
- [ ] Financial Ratios
- [ ] Earnings Analysis

---

## Portfolio

- [x] Portfolio Analysis
- [x] Diversification Analysis
- [ ] Risk Score
- [ ] Portfolio Optimization
- [ ] Sector Analysis

---

## Production

- [ ] Pydantic Tool Schemas
- [ ] Docker
- [ ] CI/CD Pipeline
- [ ] Logging & Monitoring
- [ ] Cloud Deployment

---

# Future Enhancements

- Personalized Financial Planning
- Goal-Based Investment Planning
- News Summarization Agent
- Voice Assistant
- MCP Integration
- Broker Account Integration (e.g., Zerodha)
- Portfolio Import
- Advanced Financial Analytics

---

# Author

**Shubhi Singla**

AI Finance Assistant is a personal engineering project built to explore modern AI application development using LangGraph, LangChain, Retrieval-Augmented Generation (RAG), Tool Calling, and Multi-Agent Architectures.

The project demonstrates how specialized AI agents can collaborate to solve real-world financial tasks through intelligent routing, external tools, and modular workflows.