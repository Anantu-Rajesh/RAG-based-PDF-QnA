from langchain_community.vectorstores import FAISS
from backend.embeddings import get_embeddings
from backend import config
import os

def create_vectorstore(chunks):
    """
    Create FAISS vectorstore from document chunks
    
    Args:
        chunks: List of document chunks
    
    Returns:
        FAISS: Vector store instance
    """
    # Validate input
    if not chunks:
        raise ValueError("No chunks provided for vectorstore creation")
    
    # Get embedding model
    embeddings = get_embeddings()
    
    # Create FAISS vectorstore from chunks
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    
    return vectorstore


def save_vectorstore(vectorstore):
    """
    Save vectorstore to disk
    
    Args:
        vectorstore: FAISS vectorstore instance
    """
    # Create directory if doesn't exist
    os.makedirs(config.VECTOR_DB_PATH, exist_ok=True)
    
    # Save to disk
    vectorstore.save_local(config.VECTOR_DB_PATH)
    print(f"Vectorstore saved to {config.VECTOR_DB_PATH}")


def load_vectorstore():
    """
    Load existing vectorstore from disk
    
    Returns:
        FAISS: Loaded vectorstore instance, or None if doesn't exist
    """
    index_file = os.path.join(config.VECTOR_DB_PATH, "index.faiss")
    if not os.path.exists(index_file):
        return None
    
    # Get embedding model (needed for loading)
    embeddings = get_embeddings()
    
    # Load from disk
    vectorstore = FAISS.load_local(
        config.VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    return vectorstore