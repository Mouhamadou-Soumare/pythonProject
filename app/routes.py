# routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database  
from typing import List  

router = APIRouter()


@router.get("/students/", response_model=List[schemas.Student])
def get_all_students(db: Session = Depends(database.get_db)):
    return crud.get_all_students(db)

@router.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db=db, student=student)

@router.get("/student/{identifier}", response_model=schemas.Student)
def get_student(identifier: str, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, identifier)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.delete("/student/{identifier}", response_model=dict)
def delete_student(identifier: str, db: Session = Depends(database.get_db)):
    result = crud.delete_student(db, identifier)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

@router.get("/student/{student_id}/grades", response_model=List[schemas.Grade])
def get_all_grades(student_id: str, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.get_all_grades(db, student_id)

@router.get("/student/{student_id}/grades/{grade_id}", response_model=schemas.Grade)
def get_student_grade(student_id: str, grade_id: str, db: Session = Depends(database.get_db)):
    db_grade = crud.get_grade(db, student_id, grade_id)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade

@router.post("/student/{student_id}/grades", response_model=schemas.Grade)
def create_grade(student_id: str, grade: schemas.GradeCreate, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.create_grade(db=db, student_id=student_id, grade=grade)

@router.delete("/student/{student_id}/grades/{grade_id}", response_model=dict)
def delete_grade(student_id: str, grade_id: str, db: Session = Depends(database.get_db)):
    result = crud.delete_grade(db, student_id, grade_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return {"message": "Grade deleted successfully"}