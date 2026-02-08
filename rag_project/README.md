
# 🚀 Endee-Based RAG Semantic Search Project

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Vector Search](https://img.shields.io/badge/Vector-Search-green)
![RAG](https://img.shields.io/badge/RAG-Enabled-orange)
![AI Project](https://img.shields.io/badge/AI-ML-purple)

---

## 📌 Project Title
**Retrieval Augmented Generation (RAG) Semantic Search using Endee Vector Database**

---

## 📖 Overview

This project implements a complete AI/ML pipeline using the **Endee vector database framework** to build a practical **Semantic Search + RAG (Retrieval Augmented Generation)** system.

Instead of traditional keyword matching, this system converts text into vector embeddings and performs **semantic similarity search** to retrieve the most relevant knowledge before generating answers.

The project demonstrates how vector databases power modern AI systems such as search engines, AI assistants, and knowledge retrieval tools.

---

## 🎯 Objectives

| Goal | Status |
|--------|------------|
Fork and use Endee repository | ✅ |
Build AI project using vector DB | ✅ |
Implement semantic vector search | ✅ |
Implement RAG workflow | ✅ |
Demonstrate real use case | ✅ |
Host project on GitHub | ✅ |
Provide professional README | ✅ |

---

## 🧠 Core Use Case

### ✅ Semantic Question Answering

The system:
1. Converts documents into embeddings
2. Stores them in vector storage
3. Converts user query into embedding
4. Finds most similar vectors
5. Retrieves relevant context
6. Generates context-based answer

Example:

**Query:** How is anomaly detection used in IoT security  
**System:** Retrieves related stored knowledge using vector similarity instead of keyword match.

---

## 🏗 System Architecture

```
Raw Text Data
   ↓
Embedding Model
   ↓
Vector Generation
   ↓
Vector Storage (Endee-style DB)
   ↓
Similarity Search
   ↓
Context Retrieval
   ↓
RAG Answer Generation
```

---

## 🛠 Technology Stack

| Component | Tool |
|----------------|---------------------------|
Programming Language | Python 3.9 |
Embedding Model | Sentence Transformers |
Vector Method | Dense Embeddings |
Similarity Metric | Cosine Similarity |
Storage | JSON Vector Store |
Framework Base | Endee Repository |
AI Pattern | RAG |
Use Case | Semantic Search |

---

## 📂 Project Structure

```
rag_project/
│
├── embeddings.py        → Embedding generator
├── ingest.py            → Data → vector ingestion
├── search.py            → Semantic vector search
├── app.py               → RAG answer generator
├── data.txt             → Knowledge base
├── vector_db.json       → Stored vectors
├── requirements.txt     → Dependencies
└── README.md            → Documentation
```

---

## ⚙️ Installation

### Step 1 — Install Python Libraries

```
pip install sentence-transformers
pip install numpy
pip install fastapi
pip install uvicorn
```

---

## ▶️ Execution Guide

### 🔹 Step 1 — Generate Vector Database

```
python ingest.py
```

Creates vector embeddings and stores them.

---

### 🔹 Step 2 — Run Semantic Search

```
python search.py
```

Enter natural language query → returns top semantic matches.

---

### 🔹 Step 3 — Run RAG Answer Generator

```
python app.py
```

Retrieves context + generates answer.

---

## 🧪 Sample Queries

| Query Type | Example |
|------------------|------------------------------|
Definition | What is anomaly detection |
Concept | Explain semantic search |
Technology | What is vector database |
Process | How does RAG work |
Application | Use of AI in IoT security |

---

## 📊 Output Behavior

- Returns top semantic matches
- Uses vector similarity ranking
- Retrieves context chunks
- Generates combined answer
- Demonstrates RAG pipeline

---

## 🔬 AI Concepts Demonstrated

| Concept | Demonstrated |
|-------------------------|-------------|
Vector Embeddings | ✅ |
Semantic Similarity | ✅ |
Retrieval Pipeline | ✅ |
RAG Workflow | ✅ |
Context Grounding | ✅ |
AI Search Systems | ✅ |

---

## 🚀 Future Enhancements

- Direct Endee engine API integration
- PDF and document ingestion
- Web UI interface
- LLM API integration
- Recommendation engine
- Agentic AI workflows
- Multi-document retrieval

---

## 🧾 Submission Checklist

| Requirement | Done |
|----------------------------|--------|
Endee repo forked | ✅ |
Vector search implemented | ✅ |
RAG implemented | ✅ |
Working code | ✅ |
README created | ✅ |
GitHub hosted | ✅ |

---

## ✅ Final Result

This project successfully demonstrates a **vector-search-powered AI application** using the Endee framework, implementing **Semantic Search and Retrieval Augmented Generation**, which are core building blocks of modern AI systems.

---

## 👨‍💻 Author

Assignment Submission Project — Endee Vector Database AI Use Case

