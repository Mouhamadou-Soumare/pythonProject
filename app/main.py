from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routes import router as student_router
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@mariadb/fastapi_db"

app = FastAPI()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

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

# Include the student router
app.include_router(student_router)
