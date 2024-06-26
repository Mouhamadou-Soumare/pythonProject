from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    grades = relationship("Grade", back_populates="student")

class Grade(Base):
    __tablename__ = "grades"

    id = Column(String, primary_key=True, index=True)
    course = Column(String, index=True)
    score = Column(Integer)
    student_id = Column(String, ForeignKey('students.id'))
    student = relationship("Student", back_populates="grades")
