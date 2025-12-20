# AI & LLM Engineering — Hands-on Repository

This repository documents what I have **learned and implemented** while studying modern AI and LLM engineering.

The focus is on **practical system design and hands-on implementation**, not just calling APIs.

---

## Core Skills Acquired

### Programming & Engineering Foundations
- Python programming from scratch
- Object-Oriented Programming (OOP)
- Structured data validation with Pydantic
- Git-based development workflows
- Containerized development with Docker & Docker Compose

### LLM Fundamentals
- How Large Language Models work internally
- Tokenization, embeddings, attention, and transformers
- Prompt → model → output execution flow
- Practical limitations of LLMs (context, hallucinations)

### Prompt Engineering
- Zero-shot, one-shot, and few-shot prompting
- Chain-of-thought (conceptual understanding)
- Persona-based prompts
- Structured outputs using schemas

---

## AI Systems Built

### Retrieval-Augmented Generation (RAG)
- End-to-end RAG pipelines:
  - Document loading & chunking
  - Embedding generation
  - Vector storage & retrieval
  - Answer generation
- RAG systems implemented with LangChain
- API-backed RAG services using FastAPI
- Scalable RAG patterns using queues and workers

### AI Agents
- Agents built from scratch
- Tool-using agents (LLM + external tools)
- CLI-based coding agents
- Multi-step reasoning loops (plan → act → observe)
- Reliability and failure handling

### LangGraph & Stateful AI
- Graph-based AI workflows
- Explicit state management with nodes and edges
- Checkpointing and resumable execution
- Long-running, multi-step AI systems

### Memory Systems
- Short-term and long-term memory concepts
- Vector-based semantic memory
- Episodic memory patterns
- Graph-based memory using Neo4j

### Conversational & Multi-Modal AI
- Conversational AI systems
- Speech-to-Text (STT) and Text-to-Speech (TTS)
- Voice-based AI agents
- Multi-modal inputs (text + image)

### Model Context Protocol (MCP)
- Understanding MCP and its role in AI systems

---

## Technologies Used

- **Language:** Python
- **Frameworks:** FastAPI, LangChain, LangGraph
- **LLMs:** OpenAI, Gemini, Ollama, Hugging Face
- **Datastores:** Vector DBs, Redis / Valkey, MongoDB, Neo4j
- **Infrastructure:** Docker, Docker Compose

---

## Notes
- This repository is learning-focused and iterative
- Code prioritizes clarity and correctness
- Some implementations are simplified to highlight core ideas

