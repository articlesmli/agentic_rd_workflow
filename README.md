# Agentic R&D Document Workflow

A resilient, graph-based agentic pipeline engineered to handle dense, multi-step R&D documents and clinical trial protocols[cite: 7]. This system avoids brittle, purely linear pipelines by using a state graph architecture to implement cyclical validation loops (**Extract ➔ Validate ➔ Correct ➔ Re-evaluate**)[cite: 7], with optional on-demand Model Context Protocol (MCP) tool integration.

## Architecture & Tech Stack

- **LangGraph**: Manages state orchestration, execution flow, and cyclical correction loops[cite: 7].
- **Pydantic AI**: Powers typed, production-grade LLM agents with native runtime structured enforcement[cite: 7].
- **FastAPI**: Provides a high-performance, asynchronous REST API layer for document processing[cite: 7].
- **Model Context Protocol (MCP)**: An optional, on-demand tool execution standard that connects agents to external databases and resources securely when needed.


┌──────────────────────┐
│  FastAPI Client Post │
└──────────┬───────────┘
           │ (Triggers)
           ▼
┌───────────────────────────┐
│ LangGraph State Machine   │◄────────────────┐
│ ┌───────────────────────┐ │                 │
│ │  1. extract_data      │ │                 │
│ └───────────┬───────────┘ │                 │
│             │             │                 │
│             ▼             │                 │
│ ┌───────────────────────┐ │                 │ Loopback
│ │  2. validate_data     │ │                 │ (Correction)
│ └───────────┬───────────┘ │                 │
│             │             │                 │
│             ▼             │                 │
│    /─────────────────\    │   "correct"     │
│   <  route_validation >───┼─────────────────┘
│    \─────────────────/    │
│             │             │
│             │ "finalize"  │
│             ▼             │
│          [ END ]          │
└─────────────┬─────────────┘
              │ (Returns)
              ▼
┌──────────────────────┐
│ Structured JSON Res  │
└──────────────────────┘


## Project Structure

```text
agentic-rd-workflow/
├── .github/
│   └── workflows/
│       └── ci-cd.yml      # CI/CD Automation Pipeline
├── main.py                # FastAPI application layer & endpoints
├── graph.py               # LangGraph state machine & conditional routing logic
├── agents.py              # Pydantic AI agent declarations and LLM configurations
├── schemas.py             # Pydantic data models for state, extraction, and validation
├── mcp_server.py          # Optional FastMCP server for dynamic external lookups
├── test_workflow.py       # Pytest unit and integration suite
└── requirements.txt       # Project dependencies

```

## Getting Started

### 1. Prerequisites

Ensure you have **Python 3.11+** installed on your system.

### 2. Environment Setup

Clone the repository, set up a virtual environment, and install the required dependencies:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

### 3. Configure API Keys

Set your OpenAI API key in your environment variables:

```bash
# macOS/Linux
export OPENAI_API_KEY="your-api-key-here"

# Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"

```

### 4. Run the Application

Launch the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000

```

The API will be available at `http://localhost:8000`. You can access the interactive Swagger documentation at `http://localhost:8000/docs`.

## API Usage

### Endpoint: `POST /v1/process-protocol`

#### Request Body

```json
{
  "document_text": "Phase III Trial Protocol. This study evaluates drug X. Primary objective: Measure progression-free survival over 24 weeks. Inclusion criteria: Patients must be 18-65 years old with confirmed diagnosis. Exclusion criteria: Patients under 18 are excluded. Target enrollment: 500 patients.",
  "max_validation_attempts": 3
}

```

#### Example Response (Success Case)

```json
{
  "status": "success",
  "iterations_run": 1,
  "extracted_data": {
    "phase": "Phase III",
    "primary_endpoint": "Progression-free survival over 24 weeks",
    "inclusion_criteria": ["Patients must be 18-65 years old", "Confirmed diagnosis"],
    "exclusion_criteria": ["Patients under 18 years old"],
    "sample_size": 500
  },
  "validation_summary": {
    "is_valid": true,
    "issues": [],
    "recommended_fixes": null
  }
}

```

## Testing

Run the test suite using `pytest`:

```bash
pytest

```

## CI/CD Pipeline

The project includes a GitHub Actions configuration file located in `.github/workflows/ci-cd.yml` which automates:

* **Linting**: Performs code quality verification using Ruff.


* **Testing**: Executes unit tests automatically via Pytest on every push or pull request.


* **Docker Deployment**: Automatically builds and packages your application into a Docker container, pushing the resulting artifact directly to **GitHub Container Registry (GHCR)** on every successful push to the `main` branch.



## Core Resiliency Features

* **State Retention**: Validation failures do not reset execution state. The exact downstream issues and failing structural items are retained in `AgentWorkflowState` and fed directly back to the extractor agent for targeted corrections.


* **Deterministic Circuit Breakers**: The workflow enforces a structural boundary (`max_loops`). This stops un-resolvable document ambiguities from generating infinite loops or runaway API token bills.


* **Strong Type Enforcement**: Combining LangGraph state assertions with Pydantic AI validation guarantees that schemas match exact structural expectations at node transitions before executing further pipeline cycles.


* **On-Demand MCP Integration**: External tools (such as hospital site compliance lookups) can be injected dynamically via the Model Context Protocol only when required, keeping standard document extraction fast and lightweight.

```

```
> **Note:** This project uses a custom virtual environment named `.venv_rd_mcp`. Activate it with: `source .venv-mcp/bin/activate`