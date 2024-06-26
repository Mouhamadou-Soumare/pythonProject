from sqlalchemy.orm import Session
from .models import Student, Grade
from .schemas import StudentCreate, GradeCreate
import uuid

# Prendre la DB et un Utilisateur en entrée
# Crée un nouvel utilisateur et renvoie l'utilisateur créé
def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        id=str(uuid.uuid4()), 
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Prendre la DB et l'id de l'utilisateur en entrée
# Renvoie l'utilisateur ou None si aucun utulisateur est trouvé
def get_student(db: Session, student_id: str):
    return db.query(Student).filter(Student.id == student_id).first()

# Prendre la DB et l'id de l'utilisateur en entrée
# Supprime un utilisateur et renvoie l'id de l'utilisateur supprimé
def delete_student(db: Session, student_id: str):
    db_student = get_student(db, student_id)
    if db_student is None:
        return None
    db.delete(db_student)
    db.commit()
    return student_id

# Prendre la DB et l'id de l'utilisateur en entrée
# Renvoie la liste des notes de l'utilisateur ou une erreur 404
def get_all_grades(db: Session, student_id: str):
    return db.query(Grade).filter(Grade.student_id == student_id).all()

# Prendre la DB et l'id de l'utilisateur en entrée
# Renvoie l'utilisateur
def get_grade(db: Session, student_id: str, grade_id: str):
    return db.query(Grade).filter(Grade.student_id == student_id, Grade.id == grade_id).first()

# Prendre la DB et une Note et l'ID de l'utilisateur en entrée
# Crée un nouvelle Note pour l'utilisateyr et renvoie la Note créé
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

# Prendre la DB et l'id de l'utilisateur et l'id de la Note en entrée
# Supprime la note de l'utilisateur et renvoie l'id de la Note supprimé
def delete_grade(db: Session, student_id: str, grade_id: str):
    db_grade = get_grade(db, student_id, grade_id)
    if db_grade is None:
        return None
    db.delete(db_grade)
    db.commit()
    return grade_id

# Prendre la DB en entrée
# Renvoie la liste des utilisateurs ou une erreur 404
def get_all_students(db: Session):
    return db.query(Student).all()
