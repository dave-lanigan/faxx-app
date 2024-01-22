import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pathlib import Path

from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from jinjax import Catalog

from typing import Optional

from .models import HTMLTag

from fastapi.staticfiles import StaticFiles

app = FastAPI()

nltk.download('vader_lexicon')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

catalog = Catalog()
catalog.add_folder("app/components")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return catalog.render("AppCard", app_name="Sentiment Analyzer")


@app.get("/inference")
async def get_inference(request: Request, text: str):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    print(scores)
    return scores


@app.post(
    "/inference",
    response_class=HTMLResponse,
)
async def get_inference(
    body: dict,
    hx_request: Optional[str] = Header(None),
    ):
    
    text = body["text"].strip()
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    score = scores["compound"]
    print(scores)
    
    if score > 0.5:
        emoji = "smile"
    elif score > -0.5:
        emoji = "meh"
    else:
        emoji = "frown"

    classes = ["fa-regular", f"fa-face-{emoji}", "text-6xl","text-red-300"]
    tag = HTMLTag(tag="i", classes=classes)
    return tag.dumps()