from dto.createRequest import CreateProfessorRequest
from dto.updateRequest import UpdateProfessorRequest
from fastapi import APIRouter, Depends, HTTPException, status
from model.Professor import Professor
from sqlalchemy.orm import Session
from database import get_db






router = APIRouter(prefix="/professor", tags=["Professor"])






# create professor endpoint
@router.post("/create", status_code=status.HTTP_201_CREATED)
def createProfessor(request: CreateProfessorRequest, db: Session = Depends(get_db)):
    db.add(
        Professor(request.years_of_experience, request.department, request.firstName, request.lastName, request.sex,
           request.age,
           request.phoneNumber, request.director_id))

    db.commit()
    return {"Professor SUCCESSFULLY CREATED"}


# update professor endpoint
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def updateProfessor(request: UpdateProfessorRequest, id: int, db:Session = Depends(get_db)):
    # Fetch professor from the database
    professor1db = db.get(Professor, id)

    # If the professor doesn't exist, return 404 not found
    if not professor1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    professor1data = request.dict(exclude_unset=True)

    # Update the professor's fields dynamically
    for key, value in professor1data.items():
        setattr(professor1db, key, value)

    # Save changes to the database
    db.add(professor1db)
    db.commit()
    db.refresh(professor1db)

    return professor1data


# delete student endpoint

@router.delete("/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deletePerson(id: int, db: Session = Depends(get_db)):
    professor1db = db.get(Professor, id)
    if not professor1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor  not found")
    db.delete(professor1db)
    db.commit()
    return "Professor SUCCESSFULLY DELETED"


# fetch all professors
@router.get("/getAll", status_code=status.HTTP_200_OK)
def getAllProfessors(db: Session = Depends(get_db)):
    professors = db.query(Professor).all()
    for i in range(len(professors)):
        print(professors[i].director_id)
    return professors


# get professor by id
@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def getProfessorById(id: int, db: Session = Depends(get_db)):
    professor = db.get(Professor, id)

    if not professor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")

    return professor
