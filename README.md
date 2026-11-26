# AI Career Coach — Multi-Agent System

A modular Python foundation for an AI Career Coach powered by a multi-agent architecture and Google's Gemini API (`google-genai`).

> **Project Status:** Early-stage / initial scaffolding. The core configuration, Gemini API wrapper, base agent workflow, and shared memory modules are implemented; `app.py`, `prompts/`, and `reuirments.txt` are currently placeholders under active development.

## Architecture Overview

The project is organized around decoupled components so individual agents can collaborate through shared state:

- **`config.py` (`Config`)** — Loads and validates environment configuration (`GEMINI_API_KEY` and `MODEL_NAME`, defaulting to `gemini-2.5-flash`).
- **`services/gemini_services.py` (`GeminiService`)** — Wraps the `google-genai` client (`genai.Client`) and exposes `generate_response(prompt, config=None)`.
- **`agents/base_agent.py` (`BaseAgent`)** — Abstract base class defining the standard agent lifecycle:
  1. Build a prompt from shared memory (`build_prompt`)
  2. Combine conversation context and task prompt
  3. Call `GeminiService.generate_response`
  4. Record the response in conversation memory and `SharedMemory`
- **`memory/shared_memory.py` (`SharedMemory`)** — In-memory key-value store (`add`, `get`, `exists`, `remove`, `clear`, `get_all`, `display`) for passing data between agents.

## Project Structure

```text
Ai_carrier_coach/
├── agents/
│   └── base_agent.py          # Abstract BaseAgent class
├── memory/
│   └── shared_memory.py       # SharedMemory key-value store
├── prompts/                   # Prompt templates (placeholder)
├── services/
│   └── gemini_services.py     # Gemini API client wrapper
├── app.py                     # Application entry point (placeholder)
├── config.py                  # Environment & model configuration
├── reuirments.txt             # Dependencies list (placeholder)
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Yashbagul20/AI-Carrier-Coach-Multiagent-System.git
cd AI-Carrier-Coach-Multiagent-System
```

### 2. Set up a virtual environment & install dependencies

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install google-genai python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MODEL_NAME=gemini-2.5-flash
```

> **Note:** Make sure `.env` is added to `.gitignore` before pushing commits so your API key is never exposed publicly.
