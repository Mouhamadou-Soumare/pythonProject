from uuid import UUID, uuid4
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class Grade(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    course: str
    score: int = Field(..., gt=0, le=100)

class Student(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    email: EmailStr
    grades: List[Grade] = []
