# Asset Management Copilot

AI-powered investment research assistant that enables natural language exploration of mutual fund factsheets and financial documents using Retrieval-Augmented Generation (RAG).

---

## Overview

Asset Management Copilot transforms fund factsheets into a searchable knowledge base, allowing users to ask natural language questions instead of manually reviewing multiple documents.

### Example Questions

* What is the investment objective of this fund?
* Compare ICICI Prudential and Nippon funds.
* Which fund has higher equity exposure?
* Summarize the key characteristics of this portfolio.

---

## Architecture

```text
PDF Documents
      │
      ▼
Document Ingestion
      │
      ▼
Document Chunking
      │
      ▼
Embeddings
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
LLM Response
```

---

## Technology Stack

| Component       | Technology                           |
| --------------- | ------------------------------------ |
| Language        | Python                               |
| Vector Database | ChromaDB                             |
| Retrieval       | Semantic Search                      |
| AI Pattern      | Retrieval-Augmented Generation (RAG) |
| Documents       | Mutual Fund Factsheets               |

---

## Project Structure

```text
asset-management-copilot/
│
├── app.py
├── financial_copilot.py
├── ingest.py
├── embed_documents.py
├── chunk_documents.py
├── query_documents.py
├── requirements.txt
│
├── data/
└── chroma_db/
```

---

## Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Ingestion

```bash
python ingest.py
```

### Generate Embeddings

```bash
python embed_documents.py
```

### Query Documents

```bash
python query_documents.py
```

---

## Current Features

* PDF document ingestion
* Document chunking
* Semantic retrieval
* ChromaDB vector storage
* Financial document search
* Question answering workflow

---

## Planned Enhancements

* Hugging Face embedding integration
* Advanced retrieval ranking
* Streamlit UI
* Portfolio comparison engine
* Financial analytics dashboard
* Multi-document research workflows

---

## Business Use Cases

* Asset Management
* Wealth Management
* Investment Research
* Mutual Fund Analysis
* Financial Advisory

---

## Status

Active development project focused on applying Generative AI and RAG techniques to investment research workflows.
