from model.Person import Person
from sqlalchemy import Integer, Column, String


class Professor(Person):
    __tablename__ = 'professor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    years_of_experience = Column(Integer)
    department = Column(String)

    def __init__(self, years_of_experience, department, firstName, lastName, sex, age, phoneNumber, disabled=False):
        super().__init__(firstName, lastName, sex, age, phoneNumber, disabled)
        self.years_of_experience = years_of_experience
        self.department = department
