from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    """
    Load PDF and return documents
    
    Args:
        file_path: Path to PDF file
    
    Returns:
        list: List of Document objects
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    if not documents:
        raise ValueError("PDF appears to be empty or could not be read")
    
    return documents