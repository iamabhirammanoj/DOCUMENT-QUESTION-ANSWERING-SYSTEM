from loaders.pdf_loader import load_pdf_sections
from chunking.section_chunker import chunk_documents
from embeddings.st_embeddings import STEmbeddings
from vectorstore.faiss_store import build_vectorstore
from retrieval.retriever import get_retriever
from prompting.qa_prompt import QA_PROMPT
from chains.rag_chain import run_rag

from langchain_groq import ChatGroq

import os

# -----------------------------
# CONFIG
# -----------------------------
PDF_PATH = "/media/user/New Volume/course/ChatGPT/DL/RAG/langchain_pdf_project/S25 Ultra.pdf"
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0,
)

# -----------------------------
# INGESTION (offline)
# -----------------------------
print("Loading PDF...")
docs = load_pdf_sections(PDF_PATH)

print("Chunking...")
chunks = chunk_documents(docs)

print("Embedding + building FAISS...")
embeddings = STEmbeddings()
vectorstore = build_vectorstore(chunks, embeddings)

retriever = get_retriever(vectorstore, k=4)

# -----------------------------
# LLM (Groq)
# -----------------------------
from langchain_groq import ChatGroq

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=GROQ_API_KEY,
    temperature=0,
)

# -----------------------------
# QUERY
# -----------------------------
query = "What is the camera features?"

answer, sources = run_rag(query, retriever, llm, QA_PROMPT)

print("\n===== ANSWER =====\n")
print(answer)

print("\n===== SOURCES =====\n")
for s in sources:
    print(s.metadata)
