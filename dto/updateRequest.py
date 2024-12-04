# this file will contain all the update requests of all models
from pydantic import BaseModel


# update a person request
class UpdatePersonRequest(BaseModel):
    firstName: str | None = None
    lastName: str | None = None
    sex: str | None = None
    age: int | None = None
    phoneNumber: str | None = None
