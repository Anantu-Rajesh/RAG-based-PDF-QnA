import streamlit as st
import os
from backend.utils import save_uploaded_file
from backend.loaders import load_pdf
from backend.splitter import split_documents
from backend.vectorstore import create_vectorstore, save_vectorstore, load_vectorstore
from backend.rag_chain import create_rag_chain, ask_question

# Page configuration
st.set_page_config(
    page_title="PDF Q&A with RAG",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 PDF Question Answering System")
st.markdown("Upload a PDF and ask questions about its content!")

# Sidebar for PDF upload
with st.sidebar:
    st.header("📄 Upload PDF")
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload a PDF document to ask questions about"
    )
    
    if uploaded_file is not None:
        if st.button("Process PDF", type="primary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Step 1: Save uploaded file
                    file_path = save_uploaded_file(uploaded_file, uploaded_file.name)
                    
                    # Step 2: Load PDF documents
                    documents = load_pdf(file_path)
                    
                    # Step 3: Split into chunks
                    chunks = split_documents(documents)
                    
                    # Step 4: Create vectorstore
                    vectorstore = create_vectorstore(chunks)
                    
                    # Step 5: Save vectorstore to disk
                    save_vectorstore(vectorstore)
                    
                    # Store success state
                    st.session_state.pdf_processed = True
                    st.session_state.filename = uploaded_file.name
                    st.session_state.num_pages = len(documents)
                    st.session_state.num_chunks = len(chunks)
                    
                    st.success("✅ PDF processed successfully!")
                    st.info(f"📄 Pages: {len(documents)}")
                    st.info(f"📦 Chunks created: {len(chunks)}")
                    
                except Exception as e:
                    st.error(f"Error processing PDF: {str(e)}")
    
    # Show processed PDF info
    if hasattr(st.session_state, 'pdf_processed') and st.session_state.pdf_processed:
        st.divider()
        st.success("📄 PDF Ready")
        st.write(f"**File:** {st.session_state.filename}")
        st.write(f"**Pages:** {st.session_state.num_pages}")
        st.write(f"**Chunks:** {st.session_state.num_chunks}")

# Main area for Q&A
st.divider()

# Check if PDF is processed
vectorstore = load_vectorstore()

if vectorstore is None:
    st.warning("⚠️ Please upload and process a PDF first!")
else:
    st.subheader("💬 Ask Questions")
    
    # Question input
    question = st.text_input(
        "Enter your question:",
        placeholder="e.g., What is the main topic of this document?",
        help="Ask any question about the uploaded PDF content"
    )
    
    # Ask button
    if st.button("Get Answer", type="primary", disabled=not question):
        if question:
            with st.spinner("Thinking..."):
                try:
                    # Create RAG chain
                    rag_chain = create_rag_chain(vectorstore)
                    
                    # Get answer
                    result = ask_question(rag_chain, question)
                    
                    # Display answer
                    st.success("**Answer:**")
                    st.write(result["answer"])
                    
                    # Display sources
                    with st.expander("📚 View Source Chunks"):
                        for i, doc in enumerate(result["sources"], 1):
                            st.markdown(f"**Source {i}:**")
                            st.text(doc.page_content[:300] + "...")
                            st.caption(f"Metadata: {doc.metadata}")
                            st.divider()
                
                except Exception as e:
                    st.error(f"Error getting answer: {str(e)}")