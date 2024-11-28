
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base


# creating a declarative base
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    sex = Column(String)
    age = Column(Integer)
    phoneNumber = Column(String)
    disabled = Column(Boolean)
