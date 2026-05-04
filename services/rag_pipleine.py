from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from config import GOOGLE_API_KEY

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0)

def ask_question(vectorestore,query):
    docs=vectorestore.similarity_search(query,k=3)

    context="\n".join([doc.page_content for doc in docs])

    llm=get_llm()

    prompt=f"""
   “"Answer using only the provided context. If the answer is not in the context, say "I don't know"."”
    {context}
    
    Question:{query}
    """

    response=llm.invoke(prompt)

    return response.content