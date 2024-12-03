from pydantic import BaseModel


# this file will contain all the create requests of all models


# create a person request
class CreatePersonRequest(BaseModel):
    # we are going to use BaseModel just like we learned in the first days of the learning journey

    firstName: str
    lastName: str
    sex: str
    age: int
    phoneNumber: str | None = None  # let s make the phone number Optional


# create a student request

class CreateStudentRequest(BaseModel):
    firstName: str
    lastName: str
    sex: str
    age: int
    phoneNumber: str | None = None
    department: str
    current_term: str


# create a Professor request

class CreateProfessorRequest(BaseModel):
    firstName: str
    lastName: str
    sex: str
    age: int
    phoneNumber: str | None = None
    department: str
    years_of_experience: int


# create a Director request

class CreateDirectorRequest(BaseModel):
    firstName: str
    lastName: str
    sex: str
    age: int
    phoneNumber: str | None = None
    years_of_experience: int


# create a classRoom request

class CreateClassRoomRequest(BaseModel):
    name: str
    numberOfPlaces: int
