from fastapi import FastAPI
from .database import engine, Base
from .routes import student

# Créez les tables de la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclure le routeur pour les étudiants
app.include_router(student.router, prefix="/students", tags=["students"])

@app.get("/", status_code=200)
async def root():
    return {"message": "Les notes de l'élite"}
