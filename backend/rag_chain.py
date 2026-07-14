from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from backend.llm import get_llm
from backend.retriever import get_retriever

# Custom prompt template for RAG
PROMPT_TEMPLATE = """Use the following pieces of context to answer the question at the end.
If you don't know the answer based on the context, just say that you don't know, don't try to make up an answer.

Context:
{context}

Question: {question}

Helpful Answer:"""

def create_rag_chain(vectorstore=None):
    """
    Create RAG chain combining retriever and LLM
    
    Args:
        vectorstore: FAISS vectorstore (optional)
    
    Returns:
        RetrievalQA chain
    """
    # Get components
    llm = get_llm()
    retriever = get_retriever(vectorstore)
    
    # Create custom prompt
    prompt = PromptTemplate(
        template=PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )
    
    # Create RAG chain
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return rag_chain


def ask_question(rag_chain, question):
    """
    Ask a question using the RAG chain
    
    Args:
        rag_chain: RAG chain instance
        question: User's question
    
    Returns:
        dict: Answer and source documents
    """
    result = rag_chain({"query": question})
    
    return {
        "answer": result["result"],
        "sources": result["source_documents"]
    }