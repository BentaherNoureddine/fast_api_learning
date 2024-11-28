from fastapi import FastAPI, HTTPException, status, Query
from sqlalchemy import create_engine, text, false
from sqlalchemy.orm import sessionmaker

from model.Director import Director
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

# created new instance from the person class
behe = Person("behe", "dehech", "M", 20, "+2165465445", False)

# created new instance from the director class
moudir = Director(5, "wahid", "challouf", "M", "50", "+21655530835", False)


# created a new session
session = SessionLocal()

# added the Person instance to the session
session.add(behe)

# added the Director Instance to the session
session.add(moudir)
# commited the add
session.commit()

# some tests
print(behe.firstName)


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}

# GET ALL STUDENTS ENDPOINT
