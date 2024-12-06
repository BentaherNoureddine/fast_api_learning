from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from model.ClassRoom import ClassRoom
from dto.createRequest import CreateClassRoomRequest
from dto.updateRequest import UpdateClassRoomRequest
from database import get_db

# Using APIRouter to organize routes
router = APIRouter(prefix="/classroom", tags=["classroom"])


# Create a classroom endpoint
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_classroom(request: CreateClassRoomRequest, db: Session = Depends(get_db)):

    db.add(ClassRoom(request.name,request.numberOfPlaces))
    db.commit()
    return {"message": "Classroom successfully created"}


# Update classroom endpoint
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_classroom(request: UpdateClassRoomRequest, id: int, db: Session = Depends(get_db)):
    # Fetch classroom from the database
    classroom_in_db = db.get(ClassRoom, id)

    # If the classroom doesn't exist, return 404
    if not classroom_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Classroom not found")

    # Update fields dynamically
    classroom_data = request.dict(exclude_unset=True)
    for key, value in classroom_data.items():
        setattr(classroom_in_db, key, value)

    db.commit()
    db.refresh(classroom_in_db)

    return {"message": "Classroom successfully updated", "classroom": classroom_in_db}


# Delete classroom endpoint
@router.delete("/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_classroom(id: int, db: Session = Depends(get_db)):
    classroom_in_db = db.get(ClassRoom, id)

    if not classroom_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Classroom not found")

    db.delete(classroom_in_db)
    db.commit()

    return {"message": "Classroom successfully deleted"}


# Fetch all classrooms
@router.get("/getAll", status_code=status.HTTP_200_OK)
def get_all_classrooms(db: Session = Depends(get_db)):
    classrooms = db.query(ClassRoom).all()
    return {"classrooms": classrooms}


# Get classroom by ID
@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def get_classroom_by_id(id: int, db: Session = Depends(get_db)):
    classroom = db.get(ClassRoom, id)

    if not classroom:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Classroom not found")

    return {"classroom": classroom}
