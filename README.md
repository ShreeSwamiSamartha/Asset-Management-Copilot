Asset Management Copilot

AI-powered investment research assistant that enables natural language exploration of mutual fund factsheets and financial documents.

The project demonstrates how Retrieval-Augmented Generation (RAG) can be applied to asset management workflows to reduce manual document analysis and accelerate investment research.

Problem Statement

Investment analysts and wealth managers often need to review large volumes of fund factsheets, portfolio disclosures, and performance reports.

Traditional document review is:

Time-consuming
Repetitive
Difficult to scale
Dependent on manual search

This project converts financial documents into a searchable knowledge base and enables users to ask natural language questions about fund performance, holdings, investment objectives, and portfolio characteristics.

Key Capabilities
Document Ingestion
Load fund factsheets and research documents
Extract textual content
Prepare documents for downstream processing
Document Chunking
Split documents into semantic chunks
Preserve context for retrieval
Optimize chunk size for LLM consumption
Vector Search
Convert chunks into embeddings
Store embeddings in a vector database
Retrieve relevant context using semantic similarity
Question Answering

Examples:

Which fund has the highest exposure to large-cap equities?
Compare ICICI Prudential and Nippon funds.
What is the investment objective of this fund?
Summarize key portfolio characteristics.
Current Architecture
PDF Documents
      │
      ▼
Document Ingestion
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Vector Store (ChromaDB)
      │
      ▼
Semantic Retrieval
      │
      ▼
LLM Response Generation
Technology Stack
Component	Technology
Language	Python
Vector Database	ChromaDB
Document Processing	Python PDF Libraries
Retrieval	Semantic Search
AI Pattern	Retrieval-Augmented Generation (RAG)
Repository Structure
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
Sample Workflow
Step 1

Place mutual fund factsheets inside:

data/
Step 2

Run ingestion:

python ingest.py
Step 3

Generate embeddings:

python embed_documents.py
Step 4

Query the knowledge base:

python query_documents.py
Current Limitations
Limited document set
Single-user workflow
No portfolio analytics layer
No evaluation framework for answer quality
Planned Enhancements
Near-Term
Hugging Face embedding integration
Better retrieval ranking
Improved chunking strategy
Metadata filtering
Medium-Term
Portfolio comparison engine
Fund screening assistant
Performance analytics module
Streamlit web interface
Long-Term
Multi-agent financial research workflows
Automated fund due diligence
Enterprise knowledge management integration
Business Use Cases
Asset Management
Wealth Management
Investment Research
Financial Advisory
Mutual Fund Analysis
Future Roadmap

This repository is evolving toward a domain-specific Financial Copilot capable of supporting research, comparison, summarization, and knowledge discovery across investment products.
