from sqlalchemy import Integer, Column, String
from model.Person import Person


class Student(Person):
    __tablename__ = 'student'
    department = Column(String)
    current_term = Column(String)

    #classRooms: List[ClassRoom]  I WILL DEFINE THE RELATIONSHIP LATER

    def __init__(self, department, current_term, firstName, sex, age, lastName, phoneNumber, disabled=False):
        super().__init__(firstName, sex, age, lastName, phoneNumber, disabled)
        self.department = department
        self.current_term = current_term
