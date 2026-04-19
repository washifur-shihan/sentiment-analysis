from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.routes import router as api_router
from app.api.web_routes import router as web_router

app = FastAPI(title="Sentiment Agent API", version="1.0.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(api_router, prefix="/api", tags=["sentiment"])
app.include_router(web_router, tags=["web"])