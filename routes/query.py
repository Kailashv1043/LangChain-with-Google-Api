from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_pipleine import ask_question
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


router = APIRouter()

class QueryRequest(BaseModel):
    question:str

def load_vectorstore():
    embeddings=GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

    return Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

@router.post("/ask")
def ask(req:QueryRequest):
    vectorstore=load_vectorstore()

    answer=ask_question(vectorstore,req.question)
    return{
        "answer":answer
    }