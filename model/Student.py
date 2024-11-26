from typing import List
from model.ClassRoom import ClassRoom
from model.Person import Person


class Student(Person):
    department: str
    current_term: str
    #classRooms: List[ClassRoom]  I WILL DEFINE THE RELATIONSHIP LATER

