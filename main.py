from fastapi import FastAPI, HTTPException, status, Query
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# IMPORTING PERSON AND BASE FROM PERSON.py
from model.Person import Person, Base

app = FastAPI()

# Connect to the database
host = "localhost"
username = "root"
password = ""
database = "fast_api_school"

# CREATED THE ENGINE TO ESTABLISH A CONNECTION WITH THE MYSQL DB
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}", echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}

# GET ALL STUDENTS ENDPOINT
