import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.5-flash"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
# Retrieval Configuration
TOP_K = 3  # Number of chunks to retrieve

# File paths
UPLOAD_DIR = "data/raw"
VECTOR_DB_PATH = "vector db/faiss_index"