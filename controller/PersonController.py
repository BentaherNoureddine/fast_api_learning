from fastapi import APIRouter, status, Depends
from database import get_db
from dto.createRequest import CreatePersonRequest
from dto.updateRequest import UpdatePersonRequest
from model.Person import Person
from sqlalchemy.orm import Session


# we used APIRouter to organize our code
router = APIRouter(prefix="/person", tags=["Person"])


# create a person endpoint
# added the expected status code (201)
@router.post("/create", status_code=status.HTTP_201_CREATED)
def createPerson(request: CreatePersonRequest, db: Session = Depends(get_db)):
    # create an instance of a person with the request attributes
    person1 = Person(request.firstName, request.lastName, request.sex, request.age, request.phoneNumber)

    db.add(person1)
    db.commit()
    return {"Person SUCCESSFULLY CREATED"}




# updating a person endpoint
@router.put("/person/update/{id}", status_code=status.HTTP_200_OK)
def updatePerson(request: UpdatePersonRequest, id: int, db: Session = Depends(get_db)):
    # fetch person from the database
    person1db = db.get(Person, id)

    # if the person doesn't exist, return 404 not found
    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # exclude_unset=True means that we exclude any values that would be there just for being the default values
    person1data = request.model_dump(exclude_unset=True)

    # iterating the person1data that should contain the attributes that s going to be updated with the structure
    # that we want then set those attributes in our fetched instance
    for key, value in person1data.items():
        setattr(person1db, key, value)

    db.add(person1db)
    db.commit()
    db.refresh(person1db)

    return person1data







# delete person endpoint

@router.delete("/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deletePerson(id: int, db: Session = Depends(get_db)):
    person1db = db.get(Person, id)
    if not person1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    db.delete(person1db)
    db.commit()
    return "Person SUCCESSFULLY DELETED"







# fetch all persons
@router.get("/getAll",status_code=status.HTTP_200_OK)
def getAllPerson(db: Session = Depends(get_db)):
    person = db.query(Person).all()
    return person








# get person by id
@router.get("/person/get/{id}", status_code=status.HTTP_200_OK)
def getPersonById(id: int, db: Session = Depends(get_db)):
    person = db.get(Person, id)

    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")

    return person



