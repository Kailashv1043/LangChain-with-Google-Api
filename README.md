# 🚀 Smart Knowledge Base API (RAG System)

A backend system built with FastAPI and LangChain that allows users to upload documents and ask questions based on their content using Retrieval-Augmented Generation (RAG).

---

## 🧠 Overview

This project implements a simple **RAG (Retrieval-Augmented Generation)** pipeline:

* Upload documents (PDF)
* Convert text into embeddings
* Store embeddings in a vector database
* Retrieve relevant context for user queries
* Generate answers using an LLM

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini API
* **Embeddings:** Google Generative AI Embeddings
* **Vector Database:** ChromaDB
* **Database (optional):** SQLite
* **Language:** Python

---

## ⚙️ Features

* 📄 Upload PDF documents
* 🔍 Semantic search using embeddings
* 🤖 Context-aware question answering (RAG)
* ⚡ Fast API endpoints
* 🧠 Uses real-world LLM pipeline

---

## 📂 Project Structure

```
app/
│
├── main.py
├── routes/
│   ├── upload.py
│   ├── query.py
│
├── services/
│   ├── rag_pipeline.py
│   ├── embedding.py
│
├── utils/
│   ├── file_loader.py
│   ├── chunking.py
│
├── core/
│   ├── config.py
│
└── db/
```

---

## 🔄 How It Works

1. **Upload Document**

   * PDF is loaded and split into chunks

2. **Embedding**

   * Each chunk is converted into vector embeddings

3. **Storage**

   * Stored in Chroma vector database

4. **Query**

   * User asks a question
   * System retrieves relevant chunks

5. **Response**

   * LLM generates answer using retrieved context

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-fastapi-project.git
cd rag-fastapi-project
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### 📤 Upload Document

```
POST /upload
```

Upload a PDF file.

---

### ❓ Ask Question

```
POST /ask
```

**Request:**

```json
{
  "question": "What is this document about?"
}
```

**Response:**

```json
{
  "answer": "..."
}
```

---

## ⚠️ Notes

* Ensure your PDF contains readable text (not scanned images)
* Do not expose your API key publicly
* ChromaDB stores embeddings locally in `/db`

---

## 🧠 Future Improvements

* Add chat history
* Add authentication (JWT)
* Add source citations
* Add multi-document support
* Deploy using Docker

---

## 🙌 Acknowledgements

* FastAPI
* LangChain
* Google Generative AI

---

## 📄 License

This project is for learning purposes.
