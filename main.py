from fastapi import FastAPI, HTTPException, status, Query
from sqlalchemy import create_engine, text, false
from sqlalchemy.orm import sessionmaker

from dto.createRequest import CreatePersonRequest, CreateStudentRequest, CreateProfessorRequest, CreateClassRoomRequest, \
    CreateDirectorRequest
from dto.updateRequest import UpdatePersonRequest, UpdateStudentRequest, UpdateProfessorRequest, UpdateDirectorRequest, \
    UpdateClassRoomRequest
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
def createDirector(request: CreateDirectorRequest):
    session.add(Director(request.years_of_experience, request.firstName, request.lastName, request.sex, request.age,
                         request.phoneNumber))
    session.commit()
    return {"Director SUCCESSFULLY CREATED"}


# create a classroom endpoint
@app.post("/classroom/create", status_code=status.HTTP_201_CREATED)
def createClassRoom(request: CreateClassRoomRequest):
    session.add(ClassRoom(request.name, request.numberOfPlaces))
    session.commit()
    return {"ClassRoom SUCCESSFULLY CREATED"}


# updating a person endpoint
@app.put("/person/update/{id}", status_code=status.HTTP_200_OK)
def updatePerson(request: UpdatePersonRequest, id: int):
    # fetch person from the database
    person1db = session.get(Person, id)

    # if the person doesn't exist, return 404 not found
    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # exclude_unset=True means that we exclude any values that would be there just for being the default values
    person1data = request.model_dump(exclude_unset=True)

    # iterating the person1data that should contain the attributes that s going to be updated with the structure
    # that we want then set those attributes in our fetched instance
    for key, value in person1data.items():
        setattr(person1db, key, value)

    session.add(person1db)
    session.commit()
    session.refresh(person1db)

    return person1data


# update student endpoint
@app.put("/student/update/{id}", status_code=status.HTTP_200_OK)
def updateStudent(request: UpdateStudentRequest, id: int):
    # Fetch student from the database
    student1db = session.get(Student, id)

    # If the student doesn't exist, return 404 not found
    if not student1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    student1data = request.dict(exclude_unset=True)

    # Update the student's fields dynamically
    for key, value in student1data.items():
        setattr(student1db, key, value)

    # Save changes to the database
    session.add(student1db)
    session.commit()
    session.refresh(student1db)

    return student1data


# update professor endpoint
@app.put("/professor/update/{id}", status_code=status.HTTP_200_OK)
def updateProfessor(request: UpdateProfessorRequest, id: int):
    # Fetch professor from the database
    professor1db = session.get(Professor, id)

    # If the professor doesn't exist, return 404 not found
    if not professor1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    professor1data = request.dict(exclude_unset=True)

    # Update the professor's fields dynamically
    for key, value in professor1data.items():
        setattr(professor1db, key, value)

    # Save changes to the database
    session.add(professor1db)
    session.commit()
    session.refresh(professor1db)

    return professor1data


# update director endpoint
@app.put("/director/update/{id}", status_code=status.HTTP_200_OK)
def updateDirector(request: UpdateDirectorRequest, id: int):
    # Fetch director from the database
    director1db = session.get(Director, id)

    # If the director doesn't exist, return 404 not found
    if not director1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    director1data = request.dict(exclude_unset=True)

    # Update the director's fields dynamically
    for key, value in director1data.items():
        setattr(director1db, key, value)

    # Save changes to the database
    session.add(director1db)
    session.commit()
    session.refresh(director1db)

    return director1data


# update class room endpoint

@app.put("/classroom/update/{id}", status_code=status.HTTP_200_OK)
def updateClassRoom(request: UpdateClassRoomRequest, id: int):
    # Fetch classroom from the database
    classroom1db = session.get(ClassRoom, id)

    # If the classroom doesn't exist, return 404 not found
    if not classroom1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    classroom1data = request.dict(exclude_unset=True)

    # Update the classroom's fields dynamically
    for key, value in classroom1data.items():
        setattr(classroom1db, key, value)

    # Save changes to the database
    session.add(classroom1db)
    session.commit()
    session.refresh(classroom1db)

    return classroom1data


'''

    session.add(person1)
    session.commit()

    # the refresh is responsible for refreshing the memory with the latest data from the database
    session.refresh(person1)
    return {person1}
    
'''

# todo add relationship between the classes

# todo the app should create the db if it don't exists

# todo the app should update the db schema
