from fastapi import APIRouter,UploadFile,File
import shutil
import os

from services.image_service import describe_image

router=APIRouter()

UPLOAD_DIR="upload"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/describe-image")
async def describe_image_api(file:UploadFile=File(...)):
    file_path=os.path.join(UPLOAD_DIR,file.filename)

    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

        description=describe_image(file_path)

        return{
            "filename":file.filename,
            "description":description
        }