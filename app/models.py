from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from .database import Base
import uuid

class Student(Base):
    __tablename__ = "students"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)

    grades = relationship("Grade", back_populates="student")


class Grade(Base):
    __tablename__ = "grades"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    course = Column(String(100), index=True)
    score = Column(Float)

    student_id = Column(String(36), ForeignKey('students.id'))
    student = relationship("Student", back_populates="grades")
