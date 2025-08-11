# RAG Chatbot Project Overview

## Table of Contents
- [Project Structure](#project-structure)
- [Main Components](#main-components)
- [Functionality & Data Flow](#functionality--data-flow)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Customization](#customization)
- [File-by-File Deep Dive](#file-by-file-deep-dive)

---

## Project Structure
```
rag_chatbot/
├── app.py                  # Streamlit app entrypoint (main UI and logic)
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not tracked in git)
├── modules/
│   ├── data_loader.py      # Loads and splits news from URLs
│   ├── embedding_store.py  # Handles FAISS vector store creation/loading
│   └── qa_chain.py         # Builds the QA chain using Gemini LLM
├── faiss_store_gemini/     # Saved FAISS vector store (auto-generated)
├── README.md               # Documentation
├── .gitignore, Images/, etc.
```

---

## Main Components

### `app.py` (Streamlit UI and Orchestration)
- Loads environment variables (especially `GOOGLE_API_KEY`).
- Sidebar: Lets the user input up to 3 news article URLs.
- Button: “Process URLs” triggers loading, splitting, embedding, and storing articles.
- Main Area: User can ask questions about the ingested articles.
- RAG: On question, loads the FAISS vector store, builds a QA chain, and uses Gemini LLM to answer, showing both answer and sources.

### `modules/data_loader.py`
- Function: `load_and_split_urls(urls, chunk_size=1000)`
    - Filters valid URLs.
    - Loads article content using `UnstructuredURLLoader`.
    - Splits text into manageable chunks using `RecursiveCharacterTextSplitter`.
    - Returns a list of document chunks for embedding.

### `modules/embedding_store.py`
- Function: `create_and_save_faiss(docs, file_path, api_key)`
    - Uses Gemini embeddings (`GoogleGenerativeAIEmbeddings`) to embed document chunks.
    - Stores embeddings in a local FAISS vector store.
- Function: `load_faiss(file_path, api_key)`
    - Loads the FAISS vector store with the same embedding model for retrieval.

### `modules/qa_chain.py`
- Function: `build_qa_chain(vectorstore, api_key)`
    - Instantiates a Gemini LLM (`GoogleGenerativeAI`).
    - Builds a `RetrievalQAWithSourcesChain` using LangChain, which retrieves relevant chunks and generates answers with sources.

---

## Functionality & Data Flow
1. User provides URLs → Articles loaded and split into chunks.
2. Chunks embedded using Gemini API and stored in FAISS vector store.
3. User asks a question → App loads vector store, retrieves relevant chunks, and passes them to Gemini LLM for answer generation.
4. Answer and sources displayed to the user in the UI.

This implements a classic RAG (Retrieval-Augmented Generation) pipeline:
- **Retrieval**: FAISS vector search finds relevant article chunks.
- **Generation**: Gemini LLM answers the question using retrieved context.

---

## Setup & Installation
1. **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd rag_chatbot
    ```
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Add your Google Gemini API Key**
    - Create a `.env` file in the project root:
      ```env
      GOOGLE_API_KEY=your_google_gemini_api_key_here
      ```
4. **Run the app**
    ```bash
    python -m streamlit run app.py
    ```
5. **Open in your browser**
    - Visit [http://localhost:8501](http://localhost:8501)

---

## Usage
- Paste up to 3 news article URLs in the sidebar.
- Click **Process URLs** to ingest and embed the articles.
- Ask any question about the articles in the main input box.
- The chatbot answers using Gemini-powered retrieval and shows the sources.

---

## Tech Stack
- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Unstructured](https://github.com/Unstructured-IO/unstructured)

---

## Customization
- Change the number of URLs: Edit `app.py`.
- Adjust chunk size/splitting: Edit `modules/data_loader.py`.
- Use different embedding models: Edit `modules/embedding_store.py`.

---

## File-by-File Deep Dive

### `app.py`
- **Purpose:** Main entry point and UI for the chatbot, built with Streamlit.
- **Key Responsibilities:**
    - Loads environment variables (API keys).
    - Provides a sidebar for users to input up to 3 article URLs.
    - Handles the “Process URLs” button to load, split, embed, and store articles.
    - Accepts user questions and orchestrates the retrieval and answer generation using the RAG pipeline.
    - Displays answers and their sources in the UI.
- **Logic Flow:**
    1. Load API key from `.env`.
    2. Collect URLs from sidebar.
    3. On button click: load/split articles, embed them, save to FAISS store.
    4. On question: load FAISS store, build QA chain, answer question, show sources.
    5. Handles errors (e.g., missing API key, no URLs, no FAISS store).

### `modules/data_loader.py`
- **Purpose:** Loads article content from URLs and splits them into chunks.
- **Key Responsibilities:**
    - Validates and filters user-provided URLs.
    - Uses `UnstructuredURLLoader` to fetch and parse article content.
    - Splits text into chunks (default 1000 characters) using `RecursiveCharacterTextSplitter` for efficient embedding and retrieval.
    - Returns a list of chunked documents ready for embedding.
- **Logic Flow:**
    1. Filter/validate URLs.
    2. Load articles from URLs.
    3. Split articles into chunks.
    4. Return chunked documents.

### `modules/embedding_store.py`
- **Purpose:** Handles creation and loading of the FAISS vector store for embeddings.
- **Key Responsibilities:**
    - Embeds document chunks using Google Gemini embeddings.
    - Saves embeddings to a FAISS vector store locally.
    - Loads the FAISS store and ensures embedding model consistency.
- **Logic Flow:**
    1. On create: Embed docs, save to FAISS.
    2. On load: Load FAISS with correct embedding model.
    3. Handles async event loop setup (for compatibility).

### `modules/qa_chain.py`
- **Purpose:** Builds the retrieval-augmented QA chain using LangChain and Gemini LLM.
- **Key Responsibilities:**
    - Instantiates a Gemini LLM with the provided API key.
    - Builds a `RetrievalQAWithSourcesChain` using LangChain, connecting the LLM and retriever.
    - Returns a chain object that can be invoked with user questions.
- **Logic Flow:**
    1. Instantiate Gemini LLM.
    2. Build QA chain with retriever.
    3. Return chain for use in answering questions.

### `requirements.txt`
- **Purpose:** Lists all Python dependencies required to run the project.
- **Key Packages:**
    - `streamlit`, `langchain`, `google-genai`, `langchain-google-genai`, `unstructured`, `python-dotenv`, `faiss-cpu`, `fpdf2` (for PDF export).

### `.env`
- **Purpose:** Stores sensitive environment variables (e.g., `GOOGLE_API_KEY`).
- **Usage:** Not tracked in version control for security.

### `faiss_store_gemini/`
- **Purpose:** Directory where the FAISS vector store is saved after embedding articles.
- **Usage:** Auto-generated; do not edit manually.

### `README.md`
- **Purpose:** Project documentation, setup, usage, and file explanations (this file).

---

## Summary
Your `rag_chatbot` is a modern, modular, and extensible RAG application for research and Q&A on news articles, featuring:
- Clean Streamlit UI
- Simple ingestion from URLs
- Fast retrieval with FAISS
- State-of-the-art Gemini LLM for answers with sources

---

**Happy Researching!**
