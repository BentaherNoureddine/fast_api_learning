from pydantic import BaseModel

# this file will contain all the create requests of all models
class CreatePersonRequest(BaseMdoel):
# we are going to use BaseModel just like we learned in the first days of the learning journey

      firstName: str
      lastName: str
      sex : str
      phoneNumber: str  | None= None #let s make the phone number Optional







