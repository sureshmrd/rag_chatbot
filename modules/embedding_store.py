from langchain_community.vectorstores import FAISS
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

def create_and_save_faiss(docs,file_path,api_key):
    import asyncio
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    embeddings = GoogleGenerativeAIEmbeddings(
        model = "models/embedding-001",
        google_api_key = api_key
    )
    vectorstore = FAISS.from_documents(docs,embeddings)
    vectorstore.save_local("faiss_store_gemini")

def load_faiss(file_path, api_key):
    import asyncio
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    embeddings = GoogleGenerativeAIEmbeddings(
        model = "models/embedding-001",
        google_api_key = api_key
    )
    return FAISS.load_local("faiss_store_gemini", embeddings, allow_dangerous_deserialization=True)