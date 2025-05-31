# Flowbit-Private-Limited-AI-internship

#  Multi-Agent AI System (PDF, Email, JSON Classifier & Extractor)

This project is a modular, FastAPI-based AI system that uses **LLMs** to intelligently classify documents (Email, JSON, PDF), extract relevant information, and route the input to specialized agents.

It stores all processed data in **SQLite** along with **thread IDs** for traceability and chaining.

---

##  Features

 Accepts input in **PDF**, **raw Email text**, or **structured JSON**  
 Uses Hugging Face’s **zero-shot LLM** to classify intent  
 Routes input to correct agent:
-  Email Agent: Extracts sender, urgency, and formats content
-  JSON Agent: Validates schema, flags missing fields
 Stores everything (intent, format, output, timestamp) in **SQLite**  
 Tracks **conversation/thread ID** across interactions  
 Includes interactive **Swagger UI**

---

##  System Architecture

```bash
app/
├── main.py                # FastAPI routes (/process, /logs)
├── agents/
│   ├── classifier.py      # LLM-powered intent and format classifier
│   ├── email_agent.py     # Extracts sender/urgency from emails
│   └── json_agent.py      # Validates JSON schema
├── memory/
│   ├── memory_store.py    # (optional in-memory list)
│   └── sqlite_store.py    # Stores all logs in SQLite (logs.db)
├── llm/
│   └── intent_classifier.py  # Hugging Face zero-shot classifier
└── utils/
    └── pdf_parser.py      # PDF text extractor (via pdfminer)

```

## Requirements

Python 3.8+

FastAPI

Uvicorn

requests

pdfminer.six

sqlite3 (comes with Python)

Hugging Face API token
