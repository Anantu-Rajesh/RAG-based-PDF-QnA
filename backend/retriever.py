from backend.vectorstore import load_vectorstore

def get_retriever(vectorstore=None, k=3):
    """
    Create retriever from vectorstore
    
    Args:
        vectorstore: FAISS vectorstore (if None, loads from disk)
        k: Number of top chunks to retrieve
    
    Returns:
        Retriever instance
    """
    # Load vectorstore if not provided
    if vectorstore is None:
        vectorstore = load_vectorstore()
        if vectorstore is None:
            raise ValueError("No vectorstore found. Please upload a document first.")
    
    # Create retriever with top-k configuration
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    
    return retriever


def retrieve_documents(query, retriever):
    """
    Retrieve relevant documents for a query
    
    Args:
        query: User's question
        retriever: Retriever instance
    
    Returns:
        list: List of relevant document chunks
    """
    relevant_docs = retriever.get_relevant_documents(query)
    return relevant_docs