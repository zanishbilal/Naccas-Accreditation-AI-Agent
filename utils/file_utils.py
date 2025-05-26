from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
def load_and_chunk_pdfs(directory: str, chunk_size=1000, chunk_overlap=200):
    all_chunks = []

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)
            print(f"📄 Loading: {file_path}")
            
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
            chunks = splitter.split_documents(documents)
            all_chunks.extend(chunks)

    return all_chunks
