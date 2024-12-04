from fastapi import FastAPI, HTTPException, status, Query
from sqlalchemy import create_engine, text, false
from sqlalchemy.orm import sessionmaker

from dto.createRequest import CreatePersonRequest, CreateStudentRequest, CreateProfessorRequest, CreateClassRoomRequest, \
    CreateDirectorRequest
from dto.updateRequest import UpdatePersonRequest
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

# created a new session
session = SessionLocal()


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
    session.add(
        Student(request.department, request.current_term, request.firstName, request.lastName, request.sex, request.age,
                request.phoneNumber))
    session.commit()
    return {"Student SUCCESSFULLY CREATED"}


# create professor endpoint
@app.post("/professor/create", status_code=status.HTTP_201_CREATED)
def createProfessor(request: CreateProfessorRequest):
    session.add(
        Professor(request.years_of_experience, request.department, request.firstName, request.lastName, request.sex,
                  request.age,
                  request.phoneNumber))

    session.commit()
    return {"Professor SUCCESSFULLY CREATED"}


# create director endpoint
@app.post("/director/create", status_code=status.HTTP_201_CREATED)
def createDirecor(request: CreateDirectorRequest):
    session.add(Director(request.years_of_experience, request.firstName, request.lastName, request.sex, request.age,
                         request.phoneNumber))
    session.commit()
    return {"Director SUCCESSFULLY CREATED"}


# create a classroom endpoint
@app.get("/classroom/create", status_code=status.HTTP_201_CREATED)
def createClassRoom(request: CreateClassRoomRequest):
    session.add(ClassRoom(request.name, request.numberOfPlaces))
    session.commit()
    return {"ClassRoom SUCCESSFULLY CREATED"}


@app.put("/person/update/{id}", status_code=status.HTTP_200_OK)
def updatePerson(request: UpdatePersonRequest, id: int):
    person1db = session.get(Person, id)

    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # exclude_unset=True means that we exclude any values that would be there just for being the default values
    person1data = request.model_dump(exclude_unset=True)

    person1db.sqlmodel_update = person1data

    session.add(person1db)
    session.commit()
    session.refresh(person1db)


    return {person1db}





'''
    # we're only going to update this person with the filled attributes
    if request.firstName is not None:
        person1.firstName = request.firstName
    if request.lastName is not None:
        person1.lastName = request.lastName
    if request.sex is not None:
        person1.sex = request.sex
    if request.age is not None:
        person1.age = request.age


    session.add(person1)
    session.commit()

    # the refresh is responsible for refreshing the memory with the latest data from the database
    session.refresh(person1)
    return {person1}
'''
# todo add relationship between the classes

# todo the app should create the db if it don't exists

# todo the app should update the db schema
