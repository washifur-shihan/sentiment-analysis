from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.sentiment_service import analyze_sentiment

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None,
            "text": ""
        }
    )


@router.post("/", response_class=HTMLResponse)
async def analyze_form(request: Request, text: str = Form(...)):
    result = analyze_sentiment(text)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "text": text
        }
    )