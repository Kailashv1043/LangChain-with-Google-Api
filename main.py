from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import upload,query,chat
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (ok for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload.router)
app.include_router(query.router)
app.include_router(chat.router)
