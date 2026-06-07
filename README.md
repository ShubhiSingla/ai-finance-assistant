# 💰 AI Finance Assistant

A production-ready, modular AI finance assistant powered by **LangGraph**, **LangChain**, **RAG**, and **Streamlit**.

## Architecture

```
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

| Path | Purpose |
|---|---|
| `src/agents/` | One agent class per financial domain |
| `src/rag/` | Document ingestion → chunking → embedding → retrieval |
| `src/workflow/` | LangGraph state, graph, router, and node wrappers |
| `src/tools/` | LangChain `@tool` functions (market data, calculator, news) |
| `src/web_app/` | Streamlit multi-page application |
| `src/utils/` | Logger, config loader, constants, helpers |
| `src/data/` | Raw docs, processed vector store, sample portfolios |
| `tests/` | Pytest test suites mirroring `src/` structure |

## Quick Start

```bash
# 1. Clone and enter the project
cd ai_finance_assistant

# 2. Create virtual environment
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env .env.local   # edit .env with your API keys

# 5. Run CLI
python main.py

# 6. Launch Streamlit UI
streamlit run src/web_app/app.py
```

## Configuration

All tuneable parameters live in `config.yaml`. API keys go in `.env` (never committed).

## Development Roadmap

- [ ] Implement RAG pipeline (`src/rag/`)
- [ ] Wire agent logic (`src/agents/`)
- [ ] Build LangGraph workflow (`src/workflow/graph.py`)
- [ ] Complete Streamlit pages (`src/web_app/pages/`)
- [ ] Add tool integrations (`src/tools/`)
- [ ] Write tests (`tests/`)
