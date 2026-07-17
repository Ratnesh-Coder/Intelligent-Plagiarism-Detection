# Intelligent Plagiarism Detection System

## Features
- Semantic similarity using Sentence Transformers
- N-gram Jaccard similarity
- MinHash signatures
- Winnowing fingerprints
- Locality Sensitive Hashing (LSH)
- Hybrid scoring system
- Parallel document processing
- Exact string matching (KMP, Rabin-Karp)
- Interactive HTML plagiarism report
- GUI interface

## Supported Formats
- TXT
- DOCX
- PDF

## How It Works

Query Document
↓
Preprocessing
↓
MinHash Signature
↓
LSH Candidate Search
↓
Winnowing + N-gram Similarity
↓
Semantic Similarity
↓
Hybrid Score
↓
HTML Report

## Run the Program

python main.py