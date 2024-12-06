from sqlalchemy.orm import relationship, Mapped
from model.Person import Person
from sqlalchemy import Integer, Column, ForeignKey
from model.Professor import Professor


class Director(Person):
    __tablename__ = 'director'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True, autoincrement=True)
    years_of_experience = Column(Integer)
    professors = relationship("Professor", back_populates="director",foreign_keys=[Professor.director_id])

    def __init__(self, years_of_experience, firstName, lastName, sex, age, phoneNumber, professors):
        super().__init__(firstName, lastName, sex, age, phoneNumber)
        self.years_of_experience = years_of_experience
        self.professors = professors
