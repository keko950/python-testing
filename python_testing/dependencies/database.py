from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os

dotenv.load_dotenv()

user = os.getenv("PYTHON_TESTING_DB_USER", "myuser")
password = os.getenv("PYTHON_TESTING_DB_PASSWORD", "mypassword")
host = os.getenv("PYTHON_TESTING_DB_HOST", "postgres_local")
db = os.getenv("PYTHON_TESTING_DB_NAME", "mydatabase")

DB_STRING = f"postgresql://{user}:{password}@{host}/{db}"

engine = create_engine(DB_STRING)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
