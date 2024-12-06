from fastapi import FastAPI, APIRouter, Depends, status
from dto.updateRequest import UpdateDirectorRequest
from model.Director import Director
from dto.createRequest import CreateDirectorRequest
from database import get_db
from sqlalchemy.orm import Session





# we used APIRouter to organize our code
router = APIRouter(prefix="/director", tags=["Director"])


# create director endpoint
@router.post("/create", status_code=status.HTTP_201_CREATED)
def createDirector(request: CreateDirectorRequest, db: Session = Depends(get_db)):
    db.add(Director(request.years_of_experience, request.firstName, request.lastName, request.sex, request.age,
                         request.phoneNumber, request.professors))
    db.commit()
    return {"Director SUCCESSFULLY CREATED"}


# update director endpoint
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def updateDirector(request: UpdateDirectorRequest, id: int, db: Session = Depends(get_db)):
    # Fetch director from the database
    director1db = db.get(Director, id)

    # If the director doesn't exist, return 404 not found
    if not director1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    director1data = request.dict(exclude_unset=True)

    # Update the director's fields dynamically
    for key, value in director1data.items():
        setattr(director1db, key, value)

    # Save changes to the database
    db.add(director1db)
    db.commit()
    db.refresh(director1db)

    return director1data


# fetch all directors
@router.get("/getAll", status_code=status.HTTP_200_OK)
def getAllDirector(db: Session = Depends(get_db)):
    directors = db.query(Director).all()
    for i in range(len(directors)):
        print(directors[i].professors)

    return directors


# get director by id
@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def getDirectorById(id: int, db: Session = Depends(get_db)):
    director = db.get(Director, id)

    if not director:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Director not found")

    return director
