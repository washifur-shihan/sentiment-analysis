
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Sentiment Agent API", version="1.0.0")
app.include_router(router, prefix="/api", tags=["sentiment"])