from langchain_google_genai import ChatGoogleGenerativeAI
from backend import config

def get_llm():
    """
    Create and return Gemini LLM instance
    
    Returns:
        ChatGoogleGenerativeAI: LLM model for generating answers
    """
    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL,
        google_api_key=config.GOOGLE_API_KEY,
        temperature=0.3,
        convert_system_message_to_human=True
    )
    
    return llm