from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Question(BaseModel):
    id: UUID = uuid4()
    timestamp: str = datetime.now()
    question: str
    gender: Gender
