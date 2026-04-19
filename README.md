# 🚀 Sentiment Detection Agent (RAG + NSL + FastAPI)

---

## 📌 Overview

This project is an **AI-powered sentiment analysis agent** built using a **Neuro-Symbolic + Retrieval-Augmented Generation (RAG)** approach.

It analyzes human text and returns:

* ✅ Sentiment label (positive, negative, neutral, frustrated, urgent, mixed)
* 📊 Confidence score
* 🧠 Matched symbolic rules
* 📚 Retrieved contextual evidence (via Pinecone)
* ✍️ Short natural language summary

Unlike traditional sentiment models, this system combines:

* **Symbolic rule-based reasoning (NSL)**
* **Neural embeddings (semantic understanding)**
* **Vector search (RAG with Pinecone)**

This ensures both **accuracy + controllability**.

---

## 🧠 Architecture

```text
User Input
    ↓
FastAPI Endpoint (/api/analyze)
    ↓
RAG Layer (Pinecone Retrieval)
    ↓
Feature Extraction
    ↓
Rule Engine (Symbolic Logic)
    ↓
Summary Generator
    ↓
JSON Response
```

---

## ⚙️ Tech Stack

### 🔹 Backend

* **FastAPI** – API framework
* **Uvicorn** – ASGI server

### 🔹 AI / NLP

* **Sentence Transformers (MiniLM)** – text embeddings
* **Neuro-Symbolic Logic (NSL)** – rule-based reasoning layer

### 🔹 RAG / Vector DB

* **Pinecone** – vector database for semantic retrieval

### 🔹 Other Tools

* **Pydantic** – request/response validation
* **Jinja2** – optional web UI templating
* **python-dotenv** – environment config

---

## 🧩 Core Concepts Used

### 🔹 RAG (Retrieval-Augmented Generation)

* Stores sentiment rules and knowledge in Pinecone
* Retrieves relevant context for each input
* Improves interpretability and grounding

### 🔹 NSL (Neuro-Symbolic Logic)

* Combines:

  * Neural embeddings (semantic similarity)
  * Symbolic rules (explicit logic)
* Ensures **controlled and explainable output**

### 🔹 Rule-Based Control

* Prevents model hallucination
* Ensures deterministic behavior for critical tone detection

---

## 📁 Project Structure

```text
sentiment-detection-agent/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── routes.py
│   │   └── web_routes.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   ├── services/
│   │   ├── sentiment_service.py
│   │   ├── rag_service.py
│   │   ├── pinecone_service.py
│   │   ├── embedding_service.py
│   │   ├── feature_extractor.py
│   │   ├── rule_engine.py
│   │   └── summarizer.py
│   └── data/
│       └── kb_seed.json
│
├── scripts/
│   ├── ingest_kb.py
│   └── test_retrieval.py
│
├── app/templates/
│   └── index.html
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoints

### 📌 Analyze Sentiment

```http
POST /api/analyze
```

#### Request

```json
{
  "text": "This service is broken and needs to be fixed ASAP!"
}
```

#### Response

```json
{
  "label": "urgent",
  "confidence": 0.98,
  "summary": "The text expresses urgency with negative pressure or an immediate action request.",
  "matched_rules": [
    "urgent_keywords",
    "strong_negative_words"
  ],
  "evidence": [
    "If a text contains words like urgent, asap...",
    "If a text contains words like broken..."
  ]
}
```

---

### 📌 Retrieve Evidence (Debug)

```http
POST /api/retrieve
```

---

## 🧪 How to Run Locally

### 1. Clone repo

```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add `.env`

```env
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME=sentiment-agent-index
PINECONE_NAMESPACE=sentiment-rules
```

### 5. Ingest knowledge base

```bash
python -m scripts.ingest_kb
```

### 6. Run server

```bash
uvicorn app.main:app --reload
```

### 7. Open

* Swagger UI: http://127.0.0.1:8000/docs
* Web UI: http://127.0.0.1:8000/

---

## ✨ Features

* 🔍 Semantic retrieval using embeddings
* 📚 Context-aware sentiment analysis
* ⚖️ Rule-based decision control
* 🧠 Explainable AI (matched rules + evidence)
* ⚡ FastAPI backend ready for integration
* 🌐 Optional web interface

---

## 📈 Future Improvements

* Add LLM fallback (GPT / local models)
* Multi-language support
* Better confidence calibration
* Domain-specific namespaces
* Frontend dashboard
* Docker + deployment pipeline

---

## 📜 License

MIT License

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🙌 Acknowledgements

* Pinecone (Vector DB)
* HuggingFace (Sentence Transformers)
* FastAPI ecosystem

---

## 💡 Summary

This project demonstrates a **production-style AI agent** combining:

* RAG (retrieval)
* NSL (symbolic reasoning)
* FastAPI (backend)

to deliver **accurate, controllable, and explainable sentiment analysis**.

---
