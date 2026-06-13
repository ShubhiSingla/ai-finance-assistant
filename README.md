# 💰 AI Finance Assistant

A modular multi-agent finance assistant powered by **LangGraph**, **LangChain**, **OpenAI**, **RAG**, **FAISS**, and **Streamlit**.

The system combines Retrieval-Augmented Generation (RAG), live market data tools, and multi-agent orchestration to answer financial questions, retrieve market information, and provide grounded financial guidance.

---

# Architecture

```text
                    User Query
                         │
                         ▼
                  Streamlit UI
                         │
                         ▼
                 LangGraph Workflow
                         │
                         ▼
                     Router
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
 Finance QA Agent                 Market Agent
        │                                 │
        ▼                                 ▼
    RAG Pipeline                  Yahoo Finance Tool
        │                                 │
        ▼                                 ▼
 OpenAI + Retrieved Docs        Live Market Data
        │                                 │
        └──────────────┬──────────────────┘
                       ▼
                  Final Response
                       │
                       ▼
                  Streamlit UI
```

---

# Project Structure

| Path            | Purpose                                                   |
| --------------- | --------------------------------------------------------- |
| `src/agents/`   | AI agents (Finance QA Agent, Market Agent, future agents) |
| `src/rag/`      | Document ingestion, chunking, embeddings, retrieval       |
| `src/workflow/` | LangGraph state, nodes, graph, router                     |
| `src/tools/`    | LangChain tools (market data, calculators, news, etc.)    |
| `src/web_app/`  | Streamlit application                                     |
| `src/utils/`    | Utility functions and helpers                             |
| `src/data/`     | Documents and vector database assets                      |
| `tests/`        | Pytest test suite                                         |
| `.env`          | API keys and environment variables                        |

---

# Current Capabilities

### Finance Knowledge Assistant

Ask finance-related questions such as:

* What is SIP?
* What are ETFs?
* Explain mutual funds.
* Difference between SIP and lump sum investing.

The assistant retrieves relevant financial content from its knowledge base and generates grounded responses.

---

### Live Market Intelligence

Ask market-related questions such as:

* What is Apple stock price?
* What is Tesla stock price?
* What is NVIDIA stock price?

The assistant fetches live market data using Yahoo Finance and responds using tool calling.

---

### Multi-Agent Routing

The system automatically routes user queries to the correct agent:

```text
"What is SIP?"
        ↓
 Finance QA Agent

"What is Apple stock price?"
        ↓
 Market Agent
```

---

# Implemented Features

## RAG Pipeline

* [x] URL-based document ingestion using WebBaseLoader
* [x] Financial content ingestion from Investopedia
* [x] Recursive document chunking
* [x] OpenAI embeddings (`text-embedding-3-large`)
* [x] FAISS vector database
* [x] Semantic similarity retrieval
* [x] Grounded prompt generation
* [x] Retrieval-Augmented Generation workflow

---

## Finance QA Agent

* [x] Finance-focused system prompt
* [x] RAG-powered question answering
* [x] Context-aware retrieval pipeline
* [x] Grounded financial responses

---

## Market Agent

* [x] Dedicated Market Intelligence Agent
* [x] OpenAI tool calling
* [x] Yahoo Finance integration
* [x] Live stock price retrieval
* [x] Ticker symbol support
* [x] Tool execution workflow
* [x] ToolMessage → LLM response loop

---

## LangGraph Workflow

* [x] State management
* [x] Finance QA node
* [x] Market Agent node
* [x] Router node
* [x] Conditional routing
* [x] Multi-agent orchestration

---

## Streamlit Application

* [x] Interactive web UI
* [x] LangGraph integration
* [x] RAG integration
* [x] Market Agent integration
* [x] Chat-style query interface

---

## Testing

* [x] Pytest setup
* [x] Router tests
* [x] Graph compilation tests
* [x] Market tool tests

---

## Environment & Setup

* [x] Virtual environment setup
* [x] OpenAI API integration
* [x] Environment variable management
* [x] Modular project structure
* [x] GitHub repository setup

---

# Quick Start

## Clone Repository

```bash
git clone <repo_url>

cd ai_finance_assistant
```

## Create Virtual Environment

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

## Launch Application

```bash
streamlit run src/web_app/app.py
```

---

# Example Queries

## Finance QA

```text
What is SIP?
```

```text
Explain mutual funds.
```

```text
What are ETFs?
```

```text
Difference between SIP and lump sum investing.
```

## Market Agent

```text
What is Apple stock price?
```

```text
What is Tesla stock price?
```

```text
What is NVIDIA stock price?
```

---

# Development Roadmap

## Conversational AI

* [ ] Add conversation memory
* [ ] Add chat history persistence
* [ ] Add source citations
* [ ] Add session management

---

## Router Improvements

* [ ] Upgrade keyword router to LLM router
* [ ] Add fallback routing
* [ ] Add confidence scoring
* [ ] Add routing observability

---

## Market Intelligence

* [x] Live stock prices
* [ ] Historical stock prices
* [ ] ETF analysis
* [ ] Company fundamentals
* [ ] Market trend analysis
* [ ] Financial ratios
* [ ] Earnings analysis

---

## Additional Agents

* [ ] Portfolio Analysis Agent
* [ ] Financial News Agent
* [ ] Goal Planning Agent
* [ ] Tax Agent
* [ ] Compliance Agent

---

## Advanced Features

* [ ] Personalization & Memory
* [ ] MCP Integration
* [ ] Financial Calculators
* [ ] Risk Analysis Engine
* [ ] Portfolio Optimization
* [ ] Investment Recommendation Workflows
* [ ] Voice Interface

---

## Testing & Production

* [x] Unit test framework
* [x] Router tests
* [x] Graph tests
* [ ] Integration tests
* [ ] End-to-end tests
* [ ] Logging & Monitoring
* [ ] Dockerization
* [ ] CI/CD Pipeline
* [ ] Cloud Deployment
* [ ] Performance Optimization

---

# Tech Stack

* LangChain
* LangGraph
* OpenAI GPT-4o
* OpenAI Embeddings
* FAISS
* Streamlit
* Yahoo Finance (yfinance)
* Python
* Pytest

---

# Current Status

### Completed

* RAG Pipeline
* Finance QA Agent
* Market Agent
* Yahoo Finance Tool Integration
* LangGraph Workflow
* Router
* Streamlit UI
* Automated Tests

### In Progress

* Memory
* Portfolio Agent
* Historical Market Data
* Enhanced Routing

### Planned

* News Agent
* Tax Agent
* Goal Planner Agent
* MCP Integration
* Production Deployment
