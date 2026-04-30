from fastapi import APIRouter, UploadFile, File
import os
from utils.file_loader import load_pdf
from utils.chunking import split_docs
from services.embedding import get_vectorstore

router=APIRouter()

@router.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    file_path=f"temp_{file.filename}"

    with open(file_path,"wb") as f:
        f.write(await file.read())
    
    docs=load_pdf(file_path)
    chunks=split_docs(docs)
    vectorestore=get_vectorstore(chunks)

    return {
        "message":"File uploaded and processed"
    }