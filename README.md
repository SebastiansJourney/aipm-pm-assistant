# 🤖 AIPM PM Assistant

> Describe your project. Get a full project plan, task breakdown, team allocation, risk audit, and interactive Gantt chart — autonomously.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit)](https://aipm-scheduler.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11.3-3776AB?logo=python&logoColor=white)](https://python.org)
[![LangGraph](https://img.shields.io/badge/Framework-LangGraph-1C3B5A)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/LLM-Groq%20%2F%20llama--3.3--70b-F55036)](https://groq.com)

---

## What it does

Most AI assistants answer questions. This one **manages your project.**

Give the PM Assistant a project description and a list of team members with their skills. It runs autonomously through a 6-node pipeline and delivers:

- ✅ A full task breakdown with granular subtasks
- ✅ A dependency map between all tasks
- ✅ A conflict-free project timeline
- ✅ Smart team allocation based on skills and workload
- ✅ A risk audit with mitigation suggestions
- ✅ An interactive Gantt chart (HTML output)

No manual planning. No spreadsheet juggling. Just a project plan — ready in seconds.

---

## Architecture

The agent runs a sequential multi-node pipeline using **LangGraph**:

```
Project Input (description + team)
        │
        ▼
┌─────────────────────────────────────────────┐
│              LangGraph Pipeline             │
│                                             │
│  1. Scoper  →  Breaks project into tasks    │
│       │                                     │
│  2. Mapper  →  Maps task dependencies       │
│       │                                     │
│  3. Scheduler → Builds conflict-free timeline│
│       │                                     │
│  4. Allocator → Assigns tasks by skill      │
│       │                                     │
│  5. Auditor →  Identifies risks             │
│       │                                     │
│  6. Visualizer → Generates Gantt Chart HTML │
└─────────────────────────────────────────────┘
        │
        ▼
  Interactive Gantt Chart + Project Plan
```

Each node receives the full project state, adds its output, and passes it forward. The Scheduler handles circular dependency detection automatically.

---

## Repository Structure

```
aipm-pm-assistant/
├── modular_pm_agent/              # v1 — original agent (main branch)
│   ├── main.py                    # Entry point
│   └── src/                       # Nodes, models, state, visualization
├── modular_pm_agent_v2/           # v2 — improved version (feature/improvements)
│   ├── main.py
│   └── src/
├── 1_PM_assistant_v2_Llama.ipynb  # Interactive notebook for testing
└── requirements.txt
```

---

## Versions & Branches

| Branch | Version | Description |
|---|---|---|
| `main` | v1 | Original base agent |
| `feature/improvements` | v2 | Optimizer feedback loop, improved prompts, Streamlit UI |
| `feature/ollama` | v3 (local) | Local LLM version using Ollama + Mistral — no API key needed |

---

## Prerequisites

You need a **Groq API Key** to run the agent.

1. Get a free key from [Groq](https://console.groq.com)
2. Create a `.env` file in the root directory:

```env
GROQ_API_KEY="your_api_key_here"
```

---

## Installation

**macOS / Linux**

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Windows (PowerShell)**

```powershell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Usage

**Run the full autonomous agent:**

```bash
python modular_pm_agent/main.py
```

The agent will automatically run through all 6 nodes:

1. **Scope** — Break down the project into granular tasks
2. **Map** — Identify dependencies between tasks
3. **Schedule** — Create a timeline and handle circular dependencies
4. **Allocate** — Assign tasks to team members based on skills
5. **Audit** — Assess project risks
6. **Visualize** — Generate an interactive Gantt Chart

**Open the output:**

```bash
open project_schedule.html      # macOS
# OR double-click the file in Explorer  # Windows
```

**Or use the Streamlit UI:**

```bash
streamlit run app.py
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | [LangGraph](https://github.com/langchain-ai/langgraph) |
| LLM | Groq API · llama-3.3-70b-versatile |
| Local LLM (branch) | Ollama · Mistral |
| Data Validation | Pydantic |
| UI | Streamlit |
| Output | Interactive HTML Gantt Chart |
| Language | Python 3.11.3 |

---

## Planned Improvements

- [ ] Dynamic project input via UI (no hardcoded project data)
- [ ] Workload-aware allocation (track hours per team member)
- [ ] Smarter task generation from freeform project descriptions
- [ ] Improved frontend with progress tracking
- [ ] Full local LLM support via Ollama (in progress on `feature/ollama`)

---

## Project Background

Built as part of the **AIPM Bootcamp** (neuefische, Cohort 1 · 2025/26).

Started from a coach-provided base agent and extended through two iterations — adding an optimizer feedback loop, improving LLM prompts across all nodes, and building a Streamlit interface for deployment. A third branch explores running the full pipeline locally without any external API.

This project demonstrates: multi-node agentic pipeline design with LangGraph, prompt engineering for structured JSON outputs, state management across agent nodes, and taking a local prototype to a deployed Streamlit application.

---

## Author

**Sebastian** · AIPM Bootcamp · neuefische 2025/26
[GitHub](https://github.com/SebastiansJourney) · [LinkedIn](YOUR_LINKEDIN_URL_HERE)
