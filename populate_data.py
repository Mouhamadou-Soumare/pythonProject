import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import uuid

from app.models import Base, Student, Grade

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@mariadb/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

fake = Faker()

def create_fake_student(session):
    student = Student(
        id=str(uuid.uuid4()),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email()
    )
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def create_fake_grade(session, student_id):
    grade = Grade(
        id=str(uuid.uuid4()),
        course=fake.word(),
        score=fake.random_int(min=0, max=100),
        student_id=student_id
    )
    session.add(grade)
    session.commit()

def populate_data():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    for _ in range(10): 
        student = create_fake_student(session)
        for _ in range(5): 
            create_fake_grade(session, student.id)

    session.close()

if __name__ == "__main__":
    populate_data()
