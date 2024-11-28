
from sqlalchemy import Integer, String, Column, column, true, Boolean
from pydantic import BaseModel


class Person(BaseModel):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    sex = Column(String)
    age = Column(Integer)
    phoneNumber = Column(String)
    disabled = Column(Boolean)
