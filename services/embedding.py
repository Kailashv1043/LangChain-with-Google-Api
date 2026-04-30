from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_API_KEY
import os 
import time

os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

def get_vectorstore(chunks):
    time.sleep(2)  # small delay before heavy call

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    return vectorstore