import os
from datetime import datetime
from backend import config

def save_uploaded_file(file, filename):
    """
    Save uploaded file from Streamlit to data/raw directory
    
    Args:
        file: Streamlit UploadedFile object
        filename: Original filename
    
    Returns:
        str: Path where file was saved
    """
    # Create upload directory if it doesn't exist
    os.makedirs(config.UPLOAD_DIR, exist_ok=True)
    
    # Create unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_filename = f"{timestamp}_{filename}"
    
    # Full path where file will be saved
    file_path = os.path.join(config.UPLOAD_DIR, safe_filename)
    
    # Save file to disk
    # Streamlit's UploadedFile has getvalue() or can be read as bytes
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())  # Use getbuffer() for Streamlit
    
    return file_path