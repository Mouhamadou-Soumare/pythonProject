from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@mariadb/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Use the new SQLAlchemy 2.0 API
Base = declarative_base()

# Add the get_db function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
