from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base

# creating a declarative base
# The declarative base lets us use that class in defining ORM models.
# We inherit from this base class to define our SQLAlchemy models.
# All models that inherit from this base will be mapped to corresponding tables in the database.
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    sex = Column(String(5))
    age = Column(Integer)
    phoneNumber = Column(String(50))
    disabled = Column(Boolean, default=False)

    def __init__(self, firstName, lastName, sex, age, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.age = age
        self.phoneNumber = phoneNumber

