from utils.file_utils import load_and_chunk_pdfs
from utils.text_preprocessing import get_top_k_chunks
from langchain_ollama.llms import OllamaLLM

# Load and chunk PDF policies
chunks = load_and_chunk_pdfs(r"C:\Users\kingl\OneDrive\Desktop\redlines projects\Naccas_accridation_bot\Policies")
print(f"✅ Loaded {len(chunks)} chunks.\n")

# Ask a question
query = input("❓ Enter your question: ")

# Get relevant chunks using cosine similarity
top_chunks = get_top_k_chunks(query, chunks, k=5)
context = "\n\n".join([chunk.page_content for chunk in top_chunks])

# Initialize Ollama model (use 'llama3.2:1b' or your specific model)
llm = OllamaLLM(model="qwen2.5:14b", temperature=0)

prompt = f"Answer the question using the context below:\n\n{context}\n\nQuestion: {query}"

# Call the model with the prompt string
response = llm(prompt)

print("\n🧠 Answer:\n", response)

# pine code pcsk_oJL1r_Cdxn3n6MawYbb9Z1Ft54DFhu3UxUMA1Mvk5SscGLDSbcrFHtZGKAThJRYo6kSv1
