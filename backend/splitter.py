from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend import config

def split_documents(documents):
    """
    Split documents into smaller chunks for better retrieval
    
    Args:
        documents: List of Document objects from loader
    
    Returns:
        list: List of smaller Document chunks
    """
    # Create text splitter with configured size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )
    
    # Validate input
    if not documents:
        raise ValueError("No documents provided for splitting")
    
    # Check if documents have content
    total_content = sum(len(doc.page_content.strip()) for doc in documents)
    if total_content == 0:
        raise ValueError("Documents have no text content. The PDF may be empty or contain only images.")
    
    # Split all documents into chunks
    chunks = text_splitter.split_documents(documents)
    
    # If no chunks created but we have content, it means content is shorter than chunk_size
    # In this case, return the original documents as chunks
    if not chunks and documents:
        chunks = documents
    
    if not chunks:
        raise ValueError("No chunks created from documents")
    
    return chunks