from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base

# creating a declarative base
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    sex = Column(String(50))
    age = Column(Integer)
    phoneNumber = Column(String(50))
    disabled = Column(Boolean)

    def __init__(self, firstName, lastName, sex, age, phoneNumber, disabled):

        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.age = age
        self.phoneNumber = phoneNumber
        self.disabled = disabled
