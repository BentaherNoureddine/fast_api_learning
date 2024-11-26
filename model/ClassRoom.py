from typing import List

from pydantic import BaseModel
from model.Student import Student


class ClassRoom(BaseModel):
    id: int
    name: str
    numberOfPlaces: int
    #students: List[Student] I WILL DEFINE THE RELATIONSHIP LATER
