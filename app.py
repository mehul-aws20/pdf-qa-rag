
import streamlit as st
from utils.pdf_loader import load_pdfs
from utils.vector_store import build_vectorstore
from utils.qa_chain import answer_question

st.set_page_config(page_title="PDF QA RAG", page_icon="📄")
st.title("📄 Intelligent PDF Question Answering System")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    docs = load_pdfs(uploaded_files)
    vs = build_vectorstore(docs)
    st.session_state["vs"] = vs
    st.success("Documents processed successfully.")

question = st.text_input("Ask a question about the uploaded documents")

if question and "vs" in st.session_state:
    response = answer_question(question, st.session_state["vs"])
    st.write(response)
