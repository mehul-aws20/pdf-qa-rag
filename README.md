# Intelligent PDF Question Answering System

## Overview
An NLP-based document intelligence system that allows users to upload PDF files and query them using natural language.

## Features
- PDF text extraction
- Semantic search using Sentence Transformers
- Vector similarity search using FAISS
- Interactive Streamlit interface
- Multi-document support

## Tech Stack
- Python
- Streamlit
- Sentence Transformers
- FAISS
- PyPDF2

## How It Works
1. Upload one or more PDF documents.
2. Text is extracted and divided into chunks.
3. Embeddings are generated using Sentence Transformers.
4. FAISS stores embeddings for fast retrieval.
5. User questions are matched against document content.
6. Relevant context is returned.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py