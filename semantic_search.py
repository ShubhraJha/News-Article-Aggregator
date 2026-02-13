import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
def load_model_and_index():
    with open("compressed_news.json","r",encoding="utf-8") as f:
        news = json.load(f)
    texts = [item["compressed_text"] for item in news]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return model, index, news

def search_news(query, model, index, news, k=5, min_score=0.3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    k = min(k, len(news))
    distances, indices = index.search(query_embedding, k)
    results = []
    for idx, i in enumerate(indices[0]):
        score = 1 / (1 + distances[0][idx])
        if score < min_score:   # <-- filter low similarity
            continue
        results.append({
            "title": news[i]["title"],
            "source": news[i]["source"],
            "link": news[i]["link"],  
            "summary": news[i]["compressed_text"],
            "published_at": news[i]["published_at"],
            "score": round(float(score), 3)
})
    return results

