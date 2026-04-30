from langchain_google_genai import ChatGoogleGenerativeAI
import os
from config import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def ask_question(vectorestore,query):
    docs=vectorestore.similarity_search(query,k=3)

    context="\n".join([doc.page_content for doc in docs])

    llm=get_llm()

    prompt=f"""
    Answer using only this context:
    {context}
    
    Question:{query}
    """

    response=llm.invoke(prompt)

    return response