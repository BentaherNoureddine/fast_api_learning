from fastapi import FastAPI
from pydantic import BaseModel


class PersonModel(BaseModel):
    id: int =None
    firstName: str
    lastName: str
    sex: chr
    age: int
    phoneNumber: int
    disabled: bool