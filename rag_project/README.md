
RAG Semantic Search Project using Endee Vector Database

Overview
This project demonstrates a practical AI/ML application built on top of the Endee vector database repository. It implements a Semantic Search and Retrieval Augmented Generation (RAG) workflow using vector embeddings and similarity search. The system converts text into vector embeddings, stores them, retrieves relevant content using semantic similarity, and generates context-based answers.

Assignment Requirements Covered
- Forked and used the Endee repository
- Built an AI/ML project using vector embeddings
- Implemented semantic vector search
- Implemented RAG workflow
- Demonstrated practical AI use case
- Hosted complete project on GitHub
- Provided clean documentation

Use Case Demonstrated
Semantic Search plus Retrieval Augmented Generation question answering. Instead of keyword matching, the system finds answers based on meaning using vector similarity.

Technologies Used
Python 3.9
Sentence Transformers
Vector embeddings
Cosine similarity search
JSON based vector storage
Endee repository as base framework

Project Structure
rag_project/
embeddings.py – embedding generation
ingest.py – create vector database
search.py – semantic search
app.py – RAG style answer generator
data.txt – sample data
vector_db.json – stored vectors
requirements.txt – dependencies
README.md – documentation

Installation
Install dependencies using:
pip install sentence-transformers
pip install fastapi uvicorn pypdf

How to Run

Step 1 – Ingest Data
python ingest.py

Step 2 – Run Semantic Search
python search.py

Step 3 – Run RAG App
python app.py

Example Queries
What is anomaly detection
Explain semantic search
What is a vector database
How does RAG work

Output
Returns top semantic matches, retrieves context using vector similarity, and generates an answer using retrieved knowledge.

Future Improvements
Direct Endee engine integration
PDF ingestion
Web interface
LLM API integration
Recommendation extensions

Result
This project demonstrates a working AI semantic search and RAG system where vector search is the core component implemented using Endee.

