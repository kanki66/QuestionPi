from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Question(BaseModel):
    timestamp: str = datetime.now()
    question: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/questions/")
async def create_question(question: Question):
    return question