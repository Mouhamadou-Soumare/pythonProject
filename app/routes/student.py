from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

dependence = Annotated[Session, Depends(get_db)]

# Prendre la DB en entrée
# Renvoie la liste des utilisateurs ou une erreur 404
@router.get('/', response_model=List[schemas.Student], status_code=status.HTTP_200_OK)
async def get_students(db: dependence):
    students = db.query(models.Student).all()
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Students not found')
    return students

# Prendre la DB et l'id de l'utilisateur en entrée
# Renvoie l'utilisateur ou une erreur 404
@router.get('/{student_id}', status_code=status.HTTP_200_OK)
async def get_student(student_id: str, db: dependence):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student not found')
    return student

# Prendre la DB et un utilisateur vide en entrée
# Crée un nouvel utilisateur et renvoie l'utilisateur créé
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_student(student: schemas.Student, db: dependence):
    new_student = models.Student(
        id=str(student.id),
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student

# Prendre la DB et les infos de l'utilisateur en entrée
# Met à jour un utilisateur et renvoie l'utilisateur mis à jour
@router.put('/{student_id}', status_code=status.HTTP_200_OK)
async def update_student(student_id: str, student: schemas.Student, db: dependence):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student not found')

    db_student.first_name = student.first_name
    db_student.last_name = student.last_name
    db_student.email = student.email

    db.query(models.Grade).filter(models.Grade.student_id == student_id).delete()
    for grade in student.grades:
        new_grade = models.Grade(
            course=grade.course,
            score=grade.score,
            student_id=student_id
        )
        db.add(new_grade)
    
    db.commit()
    db.refresh(db_student)
    return db_student

# Prendre la DB et l'id de l'utilisateur en entrée
# Supprime un utilisateur et renvoie l'utilisateur supprimé
@router.delete('/{student_id}', status_code=status.HTTP_200_OK)
async def delete_student(student_id: str, db: dependence):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student not found')
    
    db.delete(student)
    db.commit()
    return student

# Prendre la DB, l'id de l'utilisateur et un Grade vide en entrée
# Ajoute une note à un utilisateur et renvoie la note ajoutée
@router.post('/{student_id}/grades', response_model=schemas.Grade, status_code=status.HTTP_201_CREATED)
async def add_student_grade(student_id: str, grade: schemas.Grade, db: dependence):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Student not found')
    
    new_grade = models.Grade(
        id=str(grade.id),
        course=grade.course,
        score=grade.score,
        student_id = student.id
    )
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    
    return new_grade

# Prendre la DB l'id de la note et l'id de l'utilisateur en entrée
# Renvoie la note ou une erreur 404
@router.get('/{student_id}/grades/{grade_id}', response_model=schemas.Grade, status_code=status.HTTP_200_OK)
async def get_student_grade(student_id: str, grade_id: str, db: dependence):
    grade = db.query(models.Grade).filter(models.Grade.student_id == student_id, models.Grade.id == grade_id).first()
    if grade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Grade not found')
    
    return grade

# Prendre la DB l'id de la note et l'id de l'utilisateur en entrée
# Supprime une note et renvoie la note supprimée
@router.delete('/{student_id}/grades/{grade_id}', response_model=schemas.Grade, status_code=status.HTTP_200_OK)
async def delete_student_grade(student_id: str, grade_id: str, db: dependence):
    grade = db.query(models.Grade).filter(models.Grade.student_id == student_id, models.Grade.id == grade_id).first()
    if grade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Grade not found')
    
    db.delete(grade)
    db.commit()
    return grade
