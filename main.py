from fastapi import FastAPI
from controller.DirectorController import router as Director_router
from controller.StudentController import router as Student_router
from controller.ClassRoomController import router as ClassRoom_router
from controller.PersonController import router as Person_router
from controller.ProfessorController import router as Professor_router
from model.ClassRoom import ClassRoomBase
from database import engine
from model.Person import Base

app = FastAPI()

# we used app.include router to call all the routes
app.include_router(Director_router)
app.include_router(Student_router)
app.include_router(ClassRoom_router)
app.include_router(Person_router)
app.include_router(Professor_router)

# create the tables if they don't exist
Base.metadata.create_all(bind=engine)
# create the classroom table(the classroom is not inherited from Person class so it have to be
# created separately
ClassRoomBase.metadata.create_all(bind=engine)


# ------------------------------------------------------------------------------------------------------------------------


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}

# todo add relationship between the classes

# todo the app should create the db if it don't exists

# todo the app should update the db schema
