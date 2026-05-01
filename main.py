from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import upload,query,chat
app=FastAPI()

app.include_router(upload.router)
app.include_router(query.router)
app.include_router(chat.router)
