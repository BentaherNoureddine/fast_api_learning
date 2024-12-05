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
                  request.phoneNumber, request.director_id))

    session.commit()
    return {"Professor SUCCESSFULLY CREATED"}


# create director endpoint
@app.post("/director/create", status_code=status.HTTP_201_CREATED)
def createDirector(request: CreateDirectorRequest):
    session.add(Director(request.years_of_experience, request.firstName, request.lastName, request.sex, request.age,
                         request.phoneNumber,request.professors))
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


# delete person endpoint

@app.delete("/person/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deletePerson(id: int):
    person1db = session.get(Person, id)
    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    session.delete(person1db)
    session.commit()
    return "Person SUCCESSFULLY DELETED"


# delete student endpoint

@app.delete("/student/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deletePerson(id: int):
    student1db = session.get(Student, id)
    if not student1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    session.delete(student1db)
    session.commit()
    return "Student SUCCESSFULLY DELETED"


# delete professor endpoint

@app.delete("/professor/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deleteProfessor(id: int):
    professor1db = session.get(Professor, id)
    if not professor1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")
    session.delete(professor1db)
    session.commit()
    return "Professor SUCCESSFULLY DELETED"


# delete director endpoint

@app.delete("/director/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deleteDirector(id: int):
    director1db = session.get(Director, id)
    if not director1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Director not found")
    session.delete(director1db)
    session.commit()
    return "Director SUCCESSFULLY DELETED"


# delete classRoom endpoint

@app.delete("/classroom/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deleteClassRoom(id: int):
    director1db = session.get(ClassRoom, id)
    if not director1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Director not found")
    session.delete(director1db)
    session.commit()
    return "Director SUCCESSFULLY DELETED"


# fetch all persons
@app.get("/person/getAll", status_code=status.HTTP_200_OK)
def getAllPerson():
    person = session.query(Person).all()
    return person


# fetch all students
@app.get("/student/getAll", status_code=status.HTTP_200_OK)
def getAllStudent():
    student = session.query(Student).all()
    return student


# fetch all professors
@app.get("/professor/getAll", status_code=status.HTTP_200_OK)
def getAllProfessors():
    professors = session.query(Professor).all()
    for i in range(len(professors)):
        print(professors[i].director_id)
    return professors


# fetch all directors
@app.get("/director/getAll", status_code=status.HTTP_200_OK)
def getAllDirector():
    directors = session.query(Director).all()
    for i in range(len(directors)):
        print(directors[i].professors)

    return directors


# fetch all classRooms
@app.get("/classroom/getAll", status_code=status.HTTP_200_OK)
def getAllClassRoom():
    classroom = session.query(ClassRoom).all()
    return classroom


# get person by id
@app.get("/person/get/{id}", status_code=status.HTTP_200_OK)
def getPersonById(id: int):
    person = session.get(Person, id)

    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    return person


# get classroom by id
@app.get("/classroom/get/{id}", status_code=status.HTTP_200_OK)
def getClassRoomById(id: int):
    person = session.get(Person, id)

    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    return person


# get director by id
@app.get("/director/get/{id}", status_code=status.HTTP_200_OK)
def getDirectorById(id: int):
    director = session.get(Director, id)

    if not director:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Director not found")

    return director


# get professor by id
@app.get("/professor/get/{id}", status_code=status.HTTP_200_OK)
def getProfessorById(id: int):
    professor = session.get(Professor, id)

    if not professor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")

    return professor


# get student by id
@app.get("/student/get/{id}", status_code=status.HTTP_200_OK)
def getPersonById(id: int):
    student = session.get(Student, id)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    return student

# todo add relationship between the classes

# todo the app should create the db if it don't exists

# todo the app should update the db schema
