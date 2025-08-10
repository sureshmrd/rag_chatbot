import os
import streamlit as st
from dotenv import load_dotenv
from modules.data_loader import load_and_split_urls
from modules.embedding_store import create_and_save_faiss,load_faiss
from modules.qa_chain import build_qa_chain

#Load env vars
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
FILE_PATH = "faiss_store_gemini"

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in the environment variables")
    st.stop()

#UI
st.title("News Research Tool (Gemini API)")
st.sidebar.title("News Article URLs")

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]

if st.sidebar.button("Process URLs"):
    with st.spinner("Loading and Processing URLs...."):
        filtered_urls = [url for url in urls if url.strip()]
        docs = load_and_split_urls(filtered_urls)
        if docs:
            create_and_save_faiss(docs,FILE_PATH,GOOGLE_API_KEY)
            st.success("URLs processed successfully")
        else:
            st.warning("No valid URLs or documents found. Please enter at least one valid news article URL.")


query = st.text_input("Ask a question about the news articles")

if query :
    if os.path.exists(FILE_PATH):
        with st.spinner("Thinking..."):
            vectorstore = load_faiss(FILE_PATH, GOOGLE_API_KEY)
            chain = build_qa_chain(vectorstore,GOOGLE_API_KEY)
            result = chain.invoke({"question": query})

            st.header("Answer")
            st.write(result.get("answer", "No answer returned."))

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources")
                for src in sources.split("\n"):
                    st.write(src)
    else:
        st.warning("No FAISS store found .Please process the URLs first")
            