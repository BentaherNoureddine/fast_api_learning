from model.Person import Person
from sqlalchemy import Integer, Column, ForeignKey


class Director(Person):
    __tablename__ = 'director'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, autoincrement=True)
    years_of_experience = Column(Integer)

    def __init__(self, years_of_experience, firstName, lastName, sex, age, phoneNumber):
        super().__init__(firstName, lastName, sex, age, phoneNumber)
        self.years_of_experience = years_of_experience
