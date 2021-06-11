from typing import List 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    content: str
    coments: List[str] = []

@app.post("/article/")
def recognize_entities(article: Article):
    return {"message": f"Reading {article.content}"}
