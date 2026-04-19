from fastapi import APIRouter
from app.models.request_models import SentimentRequest
from app.models.response_models import SentimentResponse
from app.services.sentiment_service import analyze_sentiment
from app.services.rag_service import retrieve_context

router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze(payload: SentimentRequest):
    result = analyze_sentiment(payload.text)
    return SentimentResponse(**result)

@router.post("/retrieve")
async def retrieve(payload: SentimentRequest):
    return {
        "query": payload.text,
        "evidence": retrieve_context(payload.text, top_k=3)
    }