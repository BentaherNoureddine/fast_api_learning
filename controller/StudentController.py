from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from dto.updateRequest import UpdateStudentRequest
from dto.createRequest import CreateStudentRequest
from model.Student import Student

# we used APIRouter to organize our code
router = APIRouter(prefix="/student", tags=["Student"])


# create a student endpoint

@router.post("/create", status_code=status.HTTP_201_CREATED)
def createStudent(request: CreateStudentRequest, db: Session = Depends(get_db)):
    db.add(
        Student(request.department, request.current_term, request.firstName, request.lastName, request.sex, request.age,
                request.phoneNumber))
    db.commit()
    return {"Student SUCCESSFULLY CREATED"}


# update student endpoint
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def updateStudent(request: UpdateStudentRequest, id: int, db: Session = Depends(get_db)):
    # Fetch student from the database
    student1db = db.get(Student, id)

    # If the student doesn't exist, return 404 not found
    if not student1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    # Exclude unset values from the request
    student1data = request.dict(exclude_unset=True)

    # Update the student's fields dynamically
    for key, value in student1data.items():
        setattr(student1db, key, value)

    # Save changes to the database
    db.add(student1db)
    db.commit()
    db.refresh(student1db)

    return student1data


# delete student endpoint

@router.delete("/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
def deletePerson(id: int, db: Session = Depends(get_db)):
    student1db = db.get(Student, id)
    if not student1db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    db.delete(student1db)
    db.commit()
    return "Student SUCCESSFULLY DELETED"


# fetch all students
@router.get("/getAll", status_code=status.HTTP_200_OK)
def getAllStudent(db: Session = Depends(get_db)):
    student = db.query(Student).all()
    return student


# get a student by id
@router.get("/get/{id}", status_code=status.HTTP_200_OK)
def getPersonById(id: int, db: Session = Depends(get_db)):
    student = db.get(Student, id)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    return student
