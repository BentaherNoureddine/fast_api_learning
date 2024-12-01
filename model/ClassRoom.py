from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

# Define the base class for ORM models
ClassRoomBase = declarative_base()


class ClassRoom(ClassRoomBase):
    __tablename__ = 'ClassRoom'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255))
    numberOfPlaces = Column('numberOfPlaces', Integer)

    # Define the constructor
    def __init__(self, name, numberOfPlaces):
        self.name = name
        self.numberOfPlaces = numberOfPlaces

    # students: List[Student]  # I will define the relationship later
