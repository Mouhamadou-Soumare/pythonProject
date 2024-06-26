from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse
from .routes import router as student_router
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
import pandas as pd
from io import StringIO
from .database import get_db

# Importer les modèles et les routes
from .models import Base, Student, Grade
from .routes import router as student_router

# Configuration de l'URL de la base de données
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@mariadb/fastapi_db"

app = FastAPI() #Initialisation de l'application FastAPI
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Gère les connexions à la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Création d'une session locale
Base.metadata.create_all(bind=engine) # Création des tables



@app.get("/", response_class=HTMLResponse)
async def read_root(name: str = "World"):
    
    """
    Root endpoint that returns an HTML document with a greeting message.
    
    Args:
        name (str): The name to include in the greeting. Defaults to "World".
        
    Returns:
        HTMLResponse: An HTML document with the greeting message.
    """

    html_content = f"""
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <h1>Hello <span>{name}</span></h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/export")
def export_data(format: str = Query("csv", enum=["csv", "json"]), db: Session = Depends(get_db)):
    # Récupérer les données de la base de données
    students = db.query(Student).all()
    grades = db.query(Grade).all()

    # Convertir les données en DataFrame pandas
    student_data = []
    for student in students:
        for grade in student.grades:
            student_data.append({
                "student_id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "grade_id": grade.id,
                "course": grade.course,
                "score": grade.score
            })

    df = pd.DataFrame(student_data)

    if format == "csv":
        # Convertir les données en CSV
        csv_data = df.to_csv(index=False)
        response = StreamingResponse(StringIO(csv_data), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
        return response
    elif format == "json":
        # Convertir les données en JSON
        json_data = df.to_json(orient="records")
        return JSONResponse(content=json_data)

    # Si le format n'est ni CSV ni JSON, lever une erreur
    raise HTTPException(status_code=400, detail="Invalid format specified")

# Ajouter le router
app.include_router(student_router)
