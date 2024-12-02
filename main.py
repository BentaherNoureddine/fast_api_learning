from fastapi import FastAPI, HTTPException, status, Query
from sqlalchemy import create_engine, text, false
from sqlalchemy.orm import sessionmaker

from dto.createRequest import CreatePersonRequest, CreateStudentRequest
from model.Director import Director
# IMPORTING PERSON AND BASE FROM PERSON.py
from model.Person import Person, Base

from model.ClassRoom import ClassRoom, ClassRoomBase
from model.Professor import Professor
from model.Student import Student

app = FastAPI()

# Connect to the database
host = "localhost"
username = "root"
password = ""
database = "fast_api_school"

# CREATED THE ENGINE TO ESTABLISH A CONNECTION WITH THE MYSQL DB
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}", echo=True)

# Create all tables that inheritance from Person class
Base.metadata.create_all(engine)

# Create the ClassRoom Base
ClassRoomBase.metadata.create_all(engine)

# Create a session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# created new instance from the person class
behe = Person("behe", "dehech", "M", 20, "+2165465445")

# created new instance from the director class
moudir = Director(5, "wahid", "challouf", "M", "50", "+21655530835")

# created an  instance from the ClassRoom class
classRoom1 = ClassRoom("sale1", 30)

# created an instance from the Professor class
prof1 = Professor(1, "IT", "si guider", "unknown", "M", 50, "+21655530835")

# created a new session
session = SessionLocal()

# added the Person instance to the session
session.add(behe)

# added the Director Instance to the session
session.add(moudir)

# added the classRoom1 to the  session
session.add(classRoom1)

# added the pref1 to the session
session.add(prof1)

# commited the add
session.commit()

# some tests
print(behe.firstName)


# ------------------------------------------------------------------------------------------------------------------------


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}


# create a person endpoint
# added the expected status code (201)
@app.post("/person/create", status_code=status.HTTP_201_CREATED)
def createPerson(request: CreatePersonRequest):
    # create an instance of a person with the request attributes
    person1 = Person(request.firstName, request.lastName, request.sex, request.age, request.phoneNumber)

    session.add(person1)
    session.commit()
    return {"Person SUCCESSFULLY CREATED"}

# create a student endpoint

@app.post("/student/create", status_code=status.HTTP_201_CREATED)
def createStudent(request: CreateStudentRequest):
    session.add(Student(request.department, request.current_term, request.firstName, request.lastName, request.sex, request.age, request.phoneNumber))
    session.commit()
    return {"Student SUCCESSFULLY CREATED"}

