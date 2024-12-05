# this file will contain all the update requests of all models
from pydantic import BaseModel


# update a person request
class UpdatePersonRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    phoneNumber: str | None = None


# update a student request
class UpdateStudentRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    phoneNumber: str | None = None
    department: str | None = None
    current_term: str | None = None


# update a professor request
class UpdateProfessorRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    phoneNumber: str | None = None
    years_of_experience: int | None = None
    department: str | None = None


# update a director request

class UpdateDirectorRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    phoneNumber: str | None = None
    years_of_experience: int | None = None


# update class room request
class UpdateClassRoomRequest(BaseModel):
    name: str | None = None
    numberOfPlaces: int | None = None
