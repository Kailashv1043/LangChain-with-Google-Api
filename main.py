from fastapi import FastAPI

from routes import upload,query,chat,image
app=FastAPI()

app.include_router(upload.router)
app.include_router(query.router)
app.include_router(chat.router)
app.include_router(image.router)