from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_urls(urls, chunk_size=1000):
    # Filter out empty or invalid URLs
    valid_urls = [url for url in urls if isinstance(url, str) and url.strip()]
    if not valid_urls:
        return []  # or raise ValueError("No valid URLs provided")
    loader = UnstructuredURLLoader(urls=valid_urls)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ","],
        chunk_size=chunk_size,
    )
    docs = text_splitter.split_documents(data)
    return docs