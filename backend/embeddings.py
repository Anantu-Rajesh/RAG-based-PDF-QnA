#for embedding(which model being used is defined in config.py), this file is just used when we want to change data(embed it) which will be carried out in vectorstore.py 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from backend import config

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model=config.EMBEDDING_MODEL)
