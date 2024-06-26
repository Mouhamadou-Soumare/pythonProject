from sqlalchemy.orm import Session
from .models import Student, Grade
from .schemas import StudentCreate, GradeCreate
import uuid

def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        id=str(uuid.uuid4()),  # Ensure ID is generated as UUID
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.id == student_id).first()

def delete_student(db: Session, student_id: str):
    db_student = get_student(db, student_id)
    if db_student is None:
        return None
    db.delete(db_student)
    db.commit()
    return student_id

def get_all_grades(db: Session, student_id: str):
    return db.query(Grade).filter(Grade.student_id == student_id).all()

def get_grade(db: Session, student_id: str, grade_id: str):
    return db.query(Grade).filter(Grade.student_id == student_id, Grade.id == grade_id).first()

def create_grade(db: Session, student_id: str, grade: GradeCreate):
    db_grade = Grade(
        id=str(uuid.uuid4()),  # Ensure ID is generated as UUID
        course=grade.course,
        score=grade.score,
        student_id=student_id
    )
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

def delete_grade(db: Session, student_id: str, grade_id: str):
    db_grade = get_grade(db, student_id, grade_id)
    if db_grade is None:
        return None
    db.delete(db_grade)
    db.commit()
    return grade_id

def get_all_students(db: Session):
    return db.query(Student).all()
