from langchain.chains import RetrievalQAWithSourcesChain
from langchain_google_genai import GoogleGenerativeAI

def build_qa_chain(vectorstore,api_key):
    llm = GoogleGenerativeAI(
        model = "gemini-2.5-pro",
        temperature = 0.7,
        google_api_key = api_key
    )

    chain = RetrievalQAWithSourcesChain.from_llm(
       llm = llm,
       retriever = vectorstore.as_retriever()
    )

    return chain