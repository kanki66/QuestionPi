from typing import List
from fastapi import FastAPI
from models import Question
from route_homepage import general_pages_router

def start_application():
    api_ = FastAPI(debug=True)
    api_.include_router(general_pages_router)
    return api_ 

api_app = start_application()
db_quest: List[Question] = []

@api_app.get("/questions/")
async def get_questions():
    return db_quest

@api_app.post("/question/")
async def create_question(question: Question):
    db_quest.append(question)
    return question
