from pydantic import BaseModel, Field, EmailStr
from typing import List
from uuid import UUID

class GradeBase(BaseModel):
    course: str = Field(..., description="Course name")
    score: float = Field(..., ge=0, le=100, description="Score in the course (between 0 and 100)")

class GradeCreate(GradeBase):
    pass

class Grade(GradeBase):
    id: UUID = Field(..., description="Identifier for the grade")

    class Config:
        from_attributes = True

class StudentBase(BaseModel):
    first_name: str = Field(..., description="First name of the student")
    last_name: str = Field(..., description="Last name of the student")
    email: EmailStr = Field(..., description="Email address of the student")

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: UUID = Field(..., description="Identifier for the student")
    grades: List[Grade] = Field(..., description="List of grades for the student")

    class Config:
        from_attributes = True
