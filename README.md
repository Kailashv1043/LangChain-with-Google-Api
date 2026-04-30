## 💡 Why this project?

This project demonstrates a real-world RAG backend system similar to those used in:
- AI chatbots
- document assistants
- enterprise knowledge search tools

---

# 🚀 LangChain with Google API (RAG Backend)

A backend application built using FastAPI and LangChain that integrates Google Generative AI (Gemini) to perform document-based question answering using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🧠 Overview

This project demonstrates how to build a real-world LLM-powered backend system using LangChain and Google API.

It allows users to:

* Upload PDF documents
* Convert documents into embeddings
* Store embeddings in a vector database
* Ask questions based on uploaded content
* Receive context-aware answers

👉 This follows the **RAG (Retrieval-Augmented Generation)** architecture, a common pattern in modern AI systems.

---

## 🧪 Example

**Question:**
"What is this document about?"

**Answer:**
"This document explains..."

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini API
* **Framework:** LangChain
* **Vector DB:** ChromaDB
* **Database:** SQLite (optional for history)
* **Language:** Python

---

## ⚙️ Features

* 📄 Upload and process PDF documents
* ✂️ Automatic text chunking
* 🔍 Semantic search using embeddings
* 🤖 Context-based question answering
* ⚡ FastAPI-based REST endpoints
* 🧠 Real-world RAG pipeline implementation

---

## 📂 Project Structure

```bash
app/
│
├── main.py                # FastAPI entry point
│
├── routes/               # API routes
│   ├── upload.py
│   ├── query.py
│
├── services/             # Core logic
│   ├── rag_pipeline.py
│   ├── embedding.py
│
├── utils/                # Helper functions
│   ├── file_loader.py
│   ├── chunking.py
│
├── core/
│   ├── config.py         # Environment variables
│
└── db/                   # Vector DB storage
```

---

## 🔄 How It Works

1. **Document Upload**

   * User uploads a PDF via API

2. **Processing**

   * PDF → text extraction → chunking

3. **Embedding**

   * Each chunk is converted into vector embeddings

4. **Storage**

   * Stored in ChromaDB for similarity search

5. **Query**

   * User asks a question

6. **Retrieval**

   * Relevant chunks are retrieved from vector DB

7. **Answer Generation**

   * Gemini LLM generates response using context

👉 This pipeline is widely used in LLM applications ([Wikipedia][1])

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Kailashv1043/LangChain-with-Google-Api.git
cd LangChain-with-Google-Api
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install .
```

or

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open API docs

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
  "answer": "Generated answer based on document context"
}
```

---

![API Docs](screenshots/Ask_question.png)
![API Docs](screenshots/UploadDocument.png)


## ⚠️ Notes

* Only text-based PDFs are supported
* API key must be valid and active
* ChromaDB stores embeddings locally
* Avoid uploading large files initially

---

## 🧠 Future Improvements

* Add chat history
* Add authentication (JWT)
* Add source citations
* Add multi-file support
* Deploy using Docker

---

## 🙌 Acknowledgements

* LangChain (LLM framework)
* Google Generative AI (Gemini API)
* FastAPI

---

## 📄 License

This project is for learning and educational purposes.

[1]: https://en.wikipedia.org/wiki/LangChain?utm_source=chatgpt.com "LangChain"
