from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os 
import time
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def get_vectorstore(chunks):
    time.sleep(2)  

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=api_key
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    return vectorstore