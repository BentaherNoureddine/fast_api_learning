from model.Person import Person
from sqlalchemy import Integer, Column, String, ForeignKey


class Professor(Person):
    __tablename__ = 'professor'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    years_of_experience = Column(Integer)
    department = Column(String(200))

    def __init__(self, years_of_experience, department, firstName, lastName, sex, age, phoneNumber):
        super().__init__(firstName, lastName, sex, age, phoneNumber)
        self.years_of_experience = years_of_experience
        self.department = department
