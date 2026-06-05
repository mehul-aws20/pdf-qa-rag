
from sentence_transformers import SentenceTransformer
import numpy as np

def answer_question(question, vectorstore):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    q = model.encode([question])
    _, idx = vectorstore.index.search(np.array(q), k=3)
    context = "\n\n".join(vectorstore.chunks[i] for i in idx[0])
    return f"Relevant Context:\n\n{context}"
