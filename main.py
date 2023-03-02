import uvicorn

from typing import List
from fastapi import FastAPI
from models import Question

app = FastAPI(debug=True)

db_quest: List[Question] = []

@app.get("/questions/")
async def get_questions():
    return db_quest

@app.post("/questions/")
async def create_question(question: Question):
    db_quest.append(question)
    return question

if __name__ == "__main__":
    uvicorn.run(app)