# 💰 AI Finance Assistant

A production-ready, modular AI finance assistant powered by **LangGraph**, **LangChain**, **RAG**, and **Streamlit**.

## Architecture

```text
User Query → Streamlit UI → LangGraph Workflow
                                ↓
                            Router (intent classification)
                                ↓
            ┌───────────────────┼───────────────────┐
         Finance QA         Portfolio            Market
         Tax / Compliance   Goal Planner         News
                                ↓
                        RAG Pipeline (retriever → LLM)
                                ↓
                           Response → UI
```

## Project Structure

| Path            | Purpose                                                     |
| --------------- | ----------------------------------------------------------- |
| `src/agents/`   | One agent class per financial domain                        |
| `src/rag/`      | Document ingestion → chunking → embedding → retrieval       |
| `src/workflow/` | LangGraph state, graph, router, and node wrappers           |
| `src/tools/`    | LangChain `@tool` functions (market data, calculator, news) |
| `src/web_app/`  | Streamlit multi-page application                            |
| `src/utils/`    | Logger, config loader, constants, helpers                   |
| `src/data/`     | Raw docs, processed vector store, sample portfolios         |
| `tests/`        | Pytest test suites mirroring `src/` structure               |

---

# ✅ Completed Features

## RAG Pipeline

* [x] URL-based document ingestion using `WebBaseLoader`
* [x] Loaded financial educational content from Investopedia
* [x] Implemented document chunking using `RecursiveCharacterTextSplitter`
* [x] Generated embeddings using OpenAI `text-embedding-3-large`
* [x] Created FAISS vector database
* [x] Implemented semantic similarity retrieval
* [x] Built prompt generation pipeline for grounded responses

## AI Agent

* [x] Created Finance QA Agent
* [x] Connected retriever + prompt + OpenAI LLM
* [x] Implemented grounded response generation using RAG
* [x] Successfully answered finance-related questions using retrieved context

## Environment & Setup

* [x] Virtual environment setup
* [x] OpenAI API integration
* [x] Modular project structure
* [x] GitHub repository setup

---

## Quick Start

```bash
# 1. Clone and enter the project
cd ai_finance_assistant

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
python3 -m pip install -r requirements.txt

# 4. Configure environment
# Add API keys inside .env

# 5. Run project
python main.py

# 6. Launch Streamlit UI
streamlit run src/web_app/app.py
```

---

## Configuration

All tuneable parameters live in `config.yaml`.

API keys go inside `.env`:

```text
OPENAI_API_KEY=your_api_key
NEWS_API_KEY=your_news_api_key
```

---

## Development Roadmap

### Core RAG

* [x] Implement document ingestion
* [x] Implement chunking
* [x] Create embeddings
* [x] Create vector database
* [x] Implement retriever
* [x] Build Finance QA Agent

### Conversational AI

* [ ] Add conversation memory
* [ ] Build Streamlit conversational UI
* [ ] Add chat history persistence
* [ ] Add source citations in responses

### Multi-Agent System

* [ ] Build LangGraph workflow
* [ ] Add router for intent classification
* [ ] Implement Market Agent
* [ ] Implement Portfolio Agent
* [ ] Implement News Agent
* [ ] Implement Tax Agent
* [ ] Implement Goal Planner Agent
* [ ] Implement Compliance Agent

### Real-Time Integrations

* [ ] Integrate Yahoo Finance API
* [ ] Integrate News APIs
* [ ] Add real-time market analysis
* [ ] Add portfolio analytics

### Advanced Features

* [ ] Add memory and personalization
* [ ] Add MCP server integration
* [ ] Add voice interface
* [ ] Add advanced financial analytics
* [ ] Add risk analysis tools
* [ ] Add investment recommendation workflows

### Testing & Production

* [ ] Add unit tests
* [ ] Add integration tests
* [ ] Improve logging and monitoring
* [ ] Add deployment configuration
* [ ] Optimize performance
