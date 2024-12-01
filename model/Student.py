from sqlalchemy import Integer, Column, String, ForeignKey
from model.Person import Person


class Student(Person):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, autoincrement=True)
    department = Column(String(30))
    current_term = Column(String(30))

    #classRooms: List[ClassRoom]  I WILL DEFINE THE RELATIONSHIP LATER

    def __init__(self, department, current_term, firstName, sex, age, lastName, phoneNumber):
        super().__init__(firstName, sex, age, lastName, phoneNumber)
        self.department = department
        self.current_term = current_term
