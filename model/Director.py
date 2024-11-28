from model.Person import Person
from sqlalchemy import Integer, Column


class Director(Person):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    years_of_experience = Column(Integer)
