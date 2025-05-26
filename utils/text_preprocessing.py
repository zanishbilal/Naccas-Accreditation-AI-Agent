from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_top_k_chunks(query, chunks, k=5):
    texts = [chunk.page_content for chunk in chunks]
    vectorizer = TfidfVectorizer().fit(texts + [query])
    
    doc_vectors = vectorizer.transform(texts)
    query_vector = vectorizer.transform([query])
    
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    top_indices = similarities.argsort()[-k:][::-1]
    
    return [chunks[i] for i in top_indices]
