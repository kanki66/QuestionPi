from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Question
from route_homepage import general_pages_router

def start_application():
    api_ = FastAPI(debug=True)
    api_.include_router(general_pages_router)
    return api_ 

origins = ["http://localhost:8000"]
api_app = start_application()
db_quest: List[Question] = []


api_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app = start_application()

@api_app.get("/questions/")
async def get_questions():
    return db_quest

@api_app.post("/question/")
async def create_question(question: Question):
    db_quest.append(question)
    return question
