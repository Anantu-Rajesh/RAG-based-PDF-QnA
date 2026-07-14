# PDF Question Answering System with RAG

A Retrieval-Augmented Generation (RAG) application that allows you to upload PDF documents and ask questions about their content using Google's Gemini AI.

## Features

- **PDF Upload & Processing**: Upload any PDF document through an intuitive web interface
- **Intelligent Text Chunking**: Automatically splits documents into optimal chunks for retrieval
- **Vector Search**: Uses FAISS for efficient similarity search
- **AI-Powered Q&A**: Leverages Google's Gemini 2.5 Flash model for natural language responses
- **Context-Aware Answers**: Retrieves relevant document chunks to provide accurate, source-based answers
- **Interactive UI**: Clean Streamlit interface for easy interaction

## Technology Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.5 Flash
- **Embeddings**: Google Text Embedding 004
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain
- **PDF Processing**: PyPDF

## Prerequisites

- Python 3.8 or higher
- Google API Key (for Gemini AI)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "RAG mini project"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   
   > Get your API key from: https://makersuite.google.com/app/apikey

## Project Structure

```
RAG mini project/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── backend/               # Core application logic
│   ├── __init__.py
│   ├── config.py          # Configuration settings
│   ├── embeddings.py      # Embedding model setup
│   ├── llm.py             # Language model setup
│   ├── loaders.py         # PDF loading functionality
│   ├── splitter.py        # Text splitting logic
│   ├── vectorstore.py     # FAISS vector store operations
│   ├── retriever.py       # Document retrieval logic
│   ├── rag_chain.py       # RAG chain implementation
│   └── utils.py           # Utility functions
├── data/
│   └── raw/               # Uploaded PDF files (gitignored)
└── vector db/
    └── faiss_index/       # Vector database storage (gitignored)
```

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```
   Or use the virtual environment directly:
   ```bash
   .venv\Scripts\streamlit.exe run app.py
   ```

2. **Access the web interface**
   - Open your browser and go to: `http://localhost:8501`

3. **Upload and Process PDF**
   - Click "Browse files" in the sidebar
   - Select a PDF document
   - Click "Process PDF" to index the document

4. **Ask Questions**
   - Once processing is complete, type your question in the text input
   - Click "Get Answer" to receive AI-generated responses based on your document

## Configuration

Edit `backend/config.py` to customize:

- **CHUNK_SIZE**: Size of text chunks (default: 1000 characters)
- **CHUNK_OVERLAP**: Overlap between chunks (default: 200 characters)
- **TOP_K**: Number of relevant chunks to retrieve (default: 3)
- **EMBEDDING_MODEL**: Google embedding model (default: text-embedding-004)
- **LLM_MODEL**: Google LLM model (default: gemini-2.5-flash)


## How It Works

1. **Document Loading**: PDF is loaded and parsed using PyPDF
2. **Text Splitting**: Document is split into overlapping chunks for better context
3. **Embedding**: Each chunk is converted to a vector using Google's embedding model
4. **Indexing**: Vectors are stored in FAISS for fast similarity search
5. **Query Processing**: User questions are embedded and matched against document chunks
6. **Answer Generation**: Relevant chunks are sent to Gemini AI to generate contextual answers
