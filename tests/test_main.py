import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app import models

# Ensure the app directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

# Create a TestClient using the FastAPI app
client = TestClient(app)

# Create the database engine
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@mariadb/fastapi_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a new session for each test
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use a new session for each test
def override_get_db():
    try:
        db = SessionTesting()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the database tables for testing
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Set up: Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Tear down: Drop tables
    Base.metadata.drop_all(bind=engine)

def test_create_student():
    response = client.post(
        "/students/",
        json={"first_name": "eric", "last_name": "ciotti", "email": "eric.ciotti@eemi.com"}
    )
    assert response.status_code == 200
    assert response.json()["first_name"] == "eric"
    assert response.json()["last_name"] == "ciotti"
    assert response.json()["email"] == "eric.ciotti@eemi.com"

def test_get_student():
    # First, create a student
    create_response = client.post(
        "/students/",
        json={"first_name": "eric", "last_name": "ciotti", "email": "eric.ciotti@eemi.com"}
    )
    student_id = create_response.json()["id"]

    # Now, get the student
    response = client.get(f"/student/{student_id}")
    assert response.status_code == 200
    assert response.json()["first_name"] == "eric"
    assert response.json()["last_name"] == "ciotti"
    assert response.json()["email"] == "eric.ciotti@eemi.com"

def test_delete_student():
    # First, create a student
    create_response = client.post(
        "/students/",
        json={"first_name": "eric", "last_name": "ciotti", "email": "eric.ciotti@eemi.com"}
    )
    student_id = create_response.json()["id"]

    # Now, delete the student
    response = client.delete(f"/student/{student_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"

    # Verify the student is deleted
    get_response = client.get(f"/student/{student_id}")
    assert get_response.status_code == 404

def test_add_grade_to_student():
    # First, create a student
    create_response = client.post(
        "/students/",
        json={"first_name": "eric", "last_name": "ciotti", "email": "eric.ciotti@eemi.com"}
    )
    student_id = create_response.json()["id"]

    # Now, add a grade to the student
    grade_response = client.post(
        f"/student/{student_id}/grades/",
        json={"course": "Mathematics", "score": 95.0}
    )
    assert grade_response.status_code == 200
    assert grade_response.json()["course"] == "Mathematics"
    assert grade_response.json()["score"] == 95.0
    assert grade_response.json()["student_id"] == student_id
