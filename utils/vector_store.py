
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, chunks, embeddings, index):
        self.chunks = chunks
        self.embeddings = embeddings
        self.index = index

def build_vectorstore(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return VectorStore(chunks, embeddings, index)
