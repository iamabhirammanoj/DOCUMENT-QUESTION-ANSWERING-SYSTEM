from langchain.embeddings.base import Embeddings
from sentence_transformers import SentenceTransformer

class STEmbeddings(Embeddings):
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):#building the FAISS index
        return self.model.encode(texts).tolist()

    def embed_query(self, text):#embedding query
        return self.model.encode(text).tolist()
