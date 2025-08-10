<div align="center">
  <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="300" alt="Streamlit Logo"/>
  <h1>📰 News Research Chatbot (Gemini API, LangChain, FAISS)</h1>
  <p>
    <img src="https://img.shields.io/badge/Streamlit-Enabled-brightgreen?logo=streamlit" />
    <img src="https://img.shields.io/badge/LangChain-0.2+-purple?logo=python" />
    <img src="https://img.shields.io/badge/FAISS-Vector%20Search-blue" />
    <img src="https://img.shields.io/badge/Gemini%20API-Google-yellow" />
    <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  </p>
  <p>
    <b>Ask questions about news articles from URLs using Gemini embeddings and LangChain!</b>
  </p>
  <img src="<img width="2921" height="811" alt="streamlit-logo-primary-colormark-darktext" src="https://github.com/user-attachments/assets/8ea0aea1-715d-4dc0-8049-0c62433952cb" />
" width="500" alt="News Graphic"/>
</div>

---

## 🚀 Features

- 🔗 **RAG Chatbot**: Retrieve and answer questions from news articles using Retrieval-Augmented Generation.
- 🌐 **URL Loader**: Paste up to 3 news article URLs for instant analysis.
- 🧠 **Google Gemini Embeddings**: Uses Gemini API for document embeddings.
- ⚡ **FAISS Vector Store**: Fast, scalable document retrieval.
- 🦜 **LangChain**: Modern LLM orchestration and QA chain.
- 🖥️ **Streamlit UI**: Clean, interactive web interface.

---

## 📸 Demo Screenshot

<p align="center"><img width="1861" height="859" alt="Demo App Screenshot" src="https://github.com/user-attachments/assets/08289db4-99d1-44b8-8494-f4fde838d37e" />
  
</p>

---

## 🏗️ Project Structure

```
rag_chatbot/
├── app.py                  # Streamlit app entrypoint
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not tracked in git)
├── modules/
│   ├── data_loader.py      # Loads and splits news from URLs
│   ├── embedding_store.py  # Handles FAISS vector store
│   └── qa_chain.py         # Builds the QA chain
└── faiss_store_gemini/     # Saved FAISS vector store (auto-generated)
```

---

## ⚙️ Setup & Installation

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

## 📝 Usage

1. Paste up to 3 news article URLs in the sidebar.
2. Click **Process URLs** to ingest and embed the articles.
3. Ask any question about the articles in the main input box.
4. The chatbot will answer using Gemini-powered retrieval and show sources.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Unstructured](https://github.com/Unstructured-IO/unstructured)

---

## 📦 Dependencies

See [`requirements.txt`](./requirements.txt) for all packages.

---

## 💡 Customization

- Change the number of URLs by editing `app.py`.
- Adjust chunk size or split logic in `modules/data_loader.py`.
- Use different embedding models by modifying `modules/embedding_store.py`.

---

## 📄 License

This project is for educational and research purposes. Please check the licenses of the upstream dependencies for production use.

---

<div align="center">
  <img src="https://img.icons8.com/color/96/000000/artificial-intelligence.png" width="80"/>
  <br/>
  <b>Happy Researching!</b>
</div>
