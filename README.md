# RAG Basics — Ingestion & Retrieval Pipeline

A beginner-friendly **Retrieval-Augmented Generation (RAG)** project built using **LangChain, Google Gemini, and ChromaDB**.

This project demonstrates the two main stages of a RAG system:

* **Ingestion Pipeline** — Loads documents, splits them into chunks, generates embeddings, and stores them in a vector database.
* **Retrieval Pipeline** — Takes a user query, retrieves the most relevant chunks from the vector database, and uses Gemini to generate an answer.

---

## Project Structure

```text
RAG-Basics/
│
├── main.py
├── retrieval.py
├── sample_directory/
│   ├── sample.txt
│   └── test.txt
│
├── vector_db/
├── .env
└── README.md
```

* `main.py` — Ingestion Pipeline
* `retrieval.py` — Retrieval Pipeline
* `sample_directory/` — Contains sample text documents
* `vector_db/` — Locally generated Chroma vector database
* `.env` — Stores the Gemini API key locally

---

# RAG Architecture

```text
                         RAG SYSTEM
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       INGESTION PIPELINE            RETRIEVAL PIPELINE
              │                             │
              ▼                             ▼
       Load Documents                  User Query
              │                             │
              ▼                             ▼
        Split Documents              Query Embedding
              │                             │
              ▼                             ▼
       Generate Embeddings          Similarity Search
              │                             │
              ▼                             ▼
       Chroma Vector DB              Relevant Chunks
                                            │
                                            ▼
                                         Gemini
                                            │
                                            ▼
                                      Final Answer
```

---

# 1. Ingestion Pipeline

The ingestion pipeline prepares the documents before they can be searched.

```text
Text Documents
      │
      ▼
Load Documents
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
```

### Document Loading

Text files are loaded from the `sample_directory` folder using LangChain document loaders.

### Document Chunking

The loaded documents are divided into smaller chunks using `RecursiveCharacterTextSplitter`.

This makes it easier to retrieve specific pieces of information later.

### Embeddings

Google Gemini's embedding model converts each text chunk into a numerical vector representation.

### Vector Database

The chunks and their embeddings are stored in **ChromaDB**.

The generated vector database is stored locally in the `vector_db` directory.

---

# 2. Retrieval Pipeline

The retrieval pipeline searches the vector database and generates an answer based on the retrieved information.

```text
Existing Vector DB
        │
        ▼
Create Retriever
        │
        ▼
User Query
        │
        ▼
Similarity Search
        │
        ▼
Relevant Chunks
        │
        ▼
Gemini LLM
        │
        ▼
Final Answer
```

### Load Vector Database

The existing Chroma vector database created during ingestion is loaded.

### Create Retriever

The vector database is converted into a retriever that can search for relevant chunks.

### User Query

The user provides a natural-language question.

For example:

**"What is Machine Learning?"**

### Similarity Search

The query is converted into an embedding and compared with the stored embeddings.

The most relevant chunks are returned.

### Generate Answer

The retrieved chunks are provided as context to the Gemini language model.

Gemini uses the retrieved context to generate the final answer.

---

# Complete RAG Flow

```text
                 INGESTION
                    │
                    ▼
              Documents
                    │
                    ▼
                Chunking
                    │
                    ▼
               Embeddings
                    │
                    ▼
             ChromaDB
                    │
                    │
                    ▼
              RETRIEVAL
                    │
                    ▼
               User Query
                    │
                    ▼
            Query Embedding
                    │
                    ▼
           Similarity Search
                    │
                    ▼
            Relevant Chunks
                    │
                    ▼
                Gemini
                    │
                    ▼
              Final Answer
```

---

# Technologies Used

* **Python**
* **LangChain**
* **LangChain Community**
* **LangChain Text Splitters**
* **Google Gemini**
* **Google Generative AI Embeddings**
* **ChromaDB**
* **python-dotenv**

---

# Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine and open the project directory.

### 2. Install Dependencies

Install the required Python packages used by the project, including LangChain, ChromaDB, Google Gemini integration, text splitters, and `python-dotenv`.

### 3. Create a Gemini API Key

Create a Google Gemini API key through Google AI Studio.

### 4. Create the `.env` File

The `.env` file is **not pushed to GitHub** because it contains the private Gemini API key.

After cloning the project, create your own `.env` file in the root directory and add your Gemini API key using the environment variable required by the project.

**Never share or upload your API key publicly.**

### 5. Add Documents

Place your `.txt` files inside:

```text
sample_directory/
```

### 6. Run the Ingestion Pipeline

Run the ingestion pipeline first.

This will:

```text
Documents
    ↓
Chunks
    ↓
Embeddings
    ↓
ChromaDB
```

### 7. Run the Retrieval Pipeline

After the vector database has been created, run the retrieval pipeline.

This will:

```text
User Query
    ↓
Retriever
    ↓
Relevant Chunks
    ↓
Gemini
    ↓
Answer
```

---

# Environment Variables

The project requires a **Google Gemini API key**.

The `.env` file is intentionally **not included in the GitHub repository** for security reasons.

When setting up the project locally:

1. Create a `.env` file.
2. Add your own Gemini API key.
3. Save the file.
4. Run the ingestion pipeline.
5. Run the retrieval pipeline.

---

# `.gitignore`

The following should not be committed to GitHub:

```text
.env
venv/
__pycache__/
vector_db/
```

The `vector_db` directory is generated locally by the ingestion pipeline and can be recreated by running the project.

---

# Concepts Demonstrated

```text
Document Loading
       ↓
Document Chunking
       ↓
Text Embeddings
       ↓
Vector Database
       ↓
Similarity Search
       ↓
Retriever
       ↓
Context Retrieval
       ↓
LLM
       ↓
Final Answer
```

The project demonstrates:

* Document loading
* Directory-based document loading
* Text chunking
* Recursive character text splitting
* Chunk size and chunk overlap
* Embedding models
* `embed_query()`
* Vector databases
* ChromaDB
* Similarity search
* Retrievers
* Context retrieval
* LLM response generation
* RAG architecture
* Separation of ingestion and retrieval pipelines

---

# Learning Outcome

This project provides a basic understanding of how a **Retrieval-Augmented Generation system** works internally.

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
User Query
    ↓
Retrieval
    ↓
Relevant Context
    ↓
LLM
    ↓
Answer
```

---

## Author

Developed by **Ahmad Mustafa** as a learning project to understand and implement the fundamentals of **Retrieval-Augmented Generation (RAG)** using **LangChain, Google Gemini, and ChromaDB**.
