# Agentic R&D Document Workflow

A resilient, graph-based agentic pipeline and automated runtime framework designed for processing dense R&D documents, clinical trial protocols, and managing autonomous repository operations using **GitHub Agentic Workflows (`gh-aw`)**.

## Project Structure

```text
agentic_rd_workflow/
├── .github/                      # GitHub Actions & agentic workflow definitions
│   ├── aw/                       # Agentic workflow framework logs and locks
│   ├── skills/                   # Reusable workflow skills
│   └── workflows/                # CI/CD and agentic workflows (ci-cd.yml, my-first-workflow.md)
├── activation/                   # Agent activation context, prompt templates, and metadata
├── agent/                        # Runtime agent state, execution logs, MCP logs, and sandbox firewalls
├── info/                         # Workflow and run metadata
├── safe-outputs-items/           # Staged safe outputs and temporary ID maps for automated PRs
├── successful_run_artifacts/     # Captured telemetry and output metrics from successful runs
├── tests/                        # Unit and integration test suite
│   ├── test_edge_cases.py
│   ├── test_extractor.py
│   ├── test_validator.py
│   └── test_workflow.py
├── usage/                        # Token usage tracking, API rate limits, and activity summaries
├── main.py                       # FastAPI application layer & REST endpoints
├── graph.py                      # LangGraph state machine & conditional validation routing
├── agents.py                     # Pydantic AI agent declarations & LLM configurations
├── schemas.py                    # Pydantic data models for state, extraction, and validation
├── mcp_server.py                 # FastMCP server for dynamic external lookups
├── Dockerfile                    # Containerization definition
├── requirements.txt              # Python dependencies
└── REPOSITORY_HEALTH_REPORT.md   # Generated repository structure & health report

```

## Core Tech Stack

* **LangGraph**: Orchestrates execution state and cyclical correction loops (**Extract ➔ Validate ➔ Correct ➔ Re-evaluate**).
* **Pydantic AI**: Powers typed, production-grade LLM agents with native runtime structure enforcement.
* **FastAPI**: Provides a high-performance asynchronous REST API for document processing.
* **Model Context Protocol (MCP)**: Secures on-demand external tool and resource integration.
* **GitHub Agentic Workflows (`gh-aw`)**: Manages autonomous repository audits, health reports, and safe PR generation.

## Getting Started

### 1. Environment Setup

Activate your project virtual environment and install dependencies:

```bash
source .venv_a_rd_w/bin/activate  # On Windows: .venv_a_rd_w\Scripts\activate
pip install -r requirements.txt

```

### 2. Configure API Keys

Set your LLM API key:

```bash
export OPENAI_API_KEY="your-api-key-here"

```

### 3. Run the Application

Launch the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000

```

Access the interactive API docs at `http://localhost:8000/docs`.

## Testing

Run the test suite using `pytest`:

```bash
pytest

```


> **Note:** This project uses a custom virtual environment named `.venv_a_rd_w`. Activate it with: `source .venv_a_rd_w/bin/activate`

