# 🔍 Intelligent Plagiarism Detection System

### Hybrid AI and Algorithm-Based Plagiarism Detection

The **Intelligent Plagiarism Detection System** is a Python-based plagiarism detection application that combines **semantic similarity, text-matching algorithms, and document fingerprinting techniques** to identify potentially similar or plagiarized content.

The system combines modern NLP techniques with classical algorithms such as **N-gram similarity, MinHash, Winnowing, Locality Sensitive Hashing (LSH), KMP, and Rabin-Karp** to provide a multi-level plagiarism analysis.

---

## 📌 About the Project

Traditional plagiarism detection systems often rely only on exact text matching. This can fail when the same idea is rewritten using different words or sentence structures.

The **Intelligent Plagiarism Detection System** addresses this by combining multiple approaches:

- **Semantic similarity** to detect conceptually similar sentences
- **N-gram similarity** to identify overlapping phrases
- **MinHash** for efficient document similarity estimation
- **Winnowing** for document fingerprinting
- **Locality Sensitive Hashing (LSH)** for candidate document retrieval
- **KMP and Rabin-Karp** for exact pattern matching

The system processes a query document against an indexed collection of documents and generates a combined plagiarism similarity score.

---

## 🎯 Project Goals

The primary goals of the project are:

1. Detect both exact and semantically similar content.
2. Combine AI/NLP techniques with traditional string-matching algorithms.
3. Reduce unnecessary document comparisons using efficient indexing techniques.
4. Provide a hybrid plagiarism score rather than relying on a single algorithm.
5. Generate an interactive HTML report containing plagiarism analysis.
6. Provide a simple desktop interface for selecting and scanning documents.

---

## ✨ Key Features

- 🤖 Semantic similarity using Sentence Transformers
- 🔤 N-gram Jaccard similarity
- 🔢 MinHash signatures
- 🧩 Winnowing fingerprints
- ⚡ Locality Sensitive Hashing (LSH)
- 🔎 KMP exact string matching
- 🔍 Rabin-Karp exact string matching
- 🧮 Hybrid plagiarism scoring
- ⚙️ Parallel document processing
- 📄 TXT, DOCX, and PDF support
- 📊 Interactive HTML plagiarism report
- 🖥️ CustomTkinter graphical interface

---

## 🔄 How It Works

The system follows a multi-stage plagiarism detection pipeline:

```text
                    Query Document
                          │
                          ▼
                   Document Reader
                          │
                          ▼
                    Preprocessing
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        MinHash Signature       Winnowing
              │                       │
              ▼                       ▼
             LSH              Fingerprint Similarity
              │                       │
              └───────────┬───────────┘
                          ▼
                  Candidate Documents
                          │
                          ▼
                 N-gram Similarity
                          │
                          ▼
                Semantic Similarity
                          │
                          ▼
                  Hybrid Score
                          │
                          ▼
                 Exact Matching
                 ┌────────┴────────┐
                 ▼                 ▼
                KMP           Rabin-Karp
                 │                 │
                 └────────┬────────┘
                          ▼
                  HTML Report
```

---

## 🧠 Detection Techniques

### 1. Semantic Similarity

The system uses the **Sentence Transformers `all-MiniLM-L6-v2` model** to generate sentence embeddings.

Cosine similarity is then used to compare sentences from the query document with sentences from candidate documents.

This helps identify cases where content has been rewritten but retains a similar meaning.

---

### 2. N-gram Jaccard Similarity

The system generates word-based N-grams and calculates their Jaccard similarity.

The basic formula is:

```text
Jaccard Similarity =
|A ∩ B|
─────────
|A ∪ B|
```

This helps detect overlapping phrases and text structures.

---

### 3. MinHash

MinHash signatures are generated from document N-grams.

They provide an efficient approximation of document similarity without comparing every document directly.

The project uses multiple hash functions to generate a MinHash signature for each document.

---

### 4. Locality Sensitive Hashing (LSH)

LSH is used to efficiently identify documents that are likely to be similar to the query document.

Instead of performing expensive comparisons against every document, the system first retrieves likely candidates.

```text
Query Document
      │
      ▼
 MinHash Signature
      │
      ▼
      LSH
      │
      ▼
Candidate Documents
```

---

### 5. Winnowing

Winnowing generates document fingerprints by:

1. Generating k-grams
2. Hashing the k-grams
3. Creating sliding windows
4. Selecting minimum hashes as fingerprints

The resulting fingerprints are compared between documents.

---

### 6. KMP

The **Knuth-Morris-Pratt (KMP)** algorithm is used for exact pattern matching.

It identifies the positions where a given pattern occurs within the source document.

---

### 7. Rabin-Karp

The **Rabin-Karp** algorithm is also used for exact pattern matching using rolling hash values.

The project uses it alongside KMP to demonstrate and compare classical string-search approaches.

---

## 🧮 Hybrid Scoring

The final plagiarism score combines multiple similarity measurements.

The current implementation uses:

```text
Final Score =
(
    0.40 × Semantic Similarity
  + 0.25 × N-gram Similarity
  + 0.20 × Winnowing Similarity
  + 0.15 × MinHash Similarity
) × 100
```

This allows the system to consider both:

- **Meaning-based similarity**
- **Textual similarity**

rather than depending on only one detection technique.

---

## 📄 Supported File Formats

The system supports:

- `.txt`
- `.docx`
- `.pdf`

The document reader extracts the text from the selected document before sending it through the plagiarism detection pipeline.

---

## 📊 HTML Report

After completing the analysis, the system generates:

```text
plagiarism_report.html
```

The report provides a visual representation of the similarity results, including:

- Similarity scores
- Compared documents
- Similarity chart
- Overall plagiarism/original content visualization
- Matching sentence information

The generated report can be opened directly in a web browser.

---

## 🖥️ Graphical Interface

The project includes a desktop GUI built with **CustomTkinter**.

The interface provides:

- Document selection
- Plagiarism scan
- Detection status
- Progress indicator
- Result display
- HTML report access

The general workflow is:

```text
Select Document
       │
       ▼
Run Plagiarism Scan
       │
       ▼
Process Document
       │
       ▼
Run Detection Engine
       │
       ▼
Display Results
       │
       ▼
Generate HTML Report
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application |
| **Sentence Transformers** | Semantic similarity |
| **Scikit-learn** | Cosine similarity |
| **NLTK** | Text processing and tokenization |
| **CustomTkinter** | Desktop GUI |
| **python-docx** | DOCX document processing |
| **PyPDF2** | PDF document processing |
| **MinHash** | Similarity estimation |
| **Winnowing** | Document fingerprinting |
| **LSH** | Candidate document retrieval |
| **KMP** | Exact pattern matching |
| **Rabin-Karp** | Exact pattern matching |
| **HTML / JavaScript** | Interactive report |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3
- pip
- Git

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Ratnesh-Coder/Intelligent-Plagiarism-Detection.git
```

Navigate into the project:

```bash
cd Intelligent-Plagiarism-Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the application using:

```bash
python main.py
```

The CustomTkinter interface will open.

From the application:

1. Select a `.txt`, `.docx`, or `.pdf` document.
2. Click **Run Plagiarism Scan**.
3. Wait for the detection process to complete.
4. View the similarity results.
5. Open the generated HTML report.

---

## 🗂️ Document Index

The system uses a document index to improve candidate retrieval.

The index stores information such as:

- Preprocessed document text
- MinHash signatures
- Winnowing fingerprints
- LSH information

The index is stored as:

```text
document_index.pkl
```

If an index is not available, the system automatically builds one from the documents directory.

---

## 🚧 Current Limitations

The current implementation is a **prototype/research project** and has areas that can be improved.

### Detection

- The hybrid score is based on manually selected weights.
- Semantic similarity thresholds may require tuning for different domains.
- Exact matching is currently demonstrated primarily against the highest-ranked result.
- The system does not determine whether plagiarism has occurred with certainty; similarity scores indicate potentially matching content.

### Performance

- The Sentence Transformer model can require significant CPU/GPU resources.
- Large document collections may require more advanced indexing and storage strategies.

### Application

- The current interface is designed primarily for local desktop use.
- Authentication and multi-user functionality are not implemented.
- The document index is stored locally.

---

## 🎓 Project Objective

The main objective of this project is to demonstrate how **AI-based semantic analysis and classical text-processing algorithms can be combined to create a hybrid plagiarism detection system**.

Instead of relying on a single technique, the system combines:

```text
Semantic Similarity
        +
N-gram Similarity
        +
MinHash
        +
Winnowing
        +
LSH
        +
KMP
        +
Rabin-Karp
        ↓
Hybrid Plagiarism Analysis
```

This project also demonstrates practical applications of concepts from:

- Natural Language Processing
- Machine Learning
- Data Structures and Algorithms
- Information Retrieval
- Document Fingerprinting
- Similarity Search

---

## 👨‍💻 Author

**Ratnesh**

Engineering Student

GitHub:  
https://github.com/Ratnesh-Coder

---

## 📄 License

This project is currently maintained as a personal/student project.

If a formal open-source license is added in the future, the license information will be updated here.

---

### 🔍 Intelligent Plagiarism Detection System

**Combining AI-powered semantic analysis with classical algorithms for intelligent plagiarism detection.**
