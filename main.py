from fastapi import FastAPI, HTTPException, status, Query
import mysql.connector

app = FastAPI()

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fast_api_school"
)

# Create a cursor object
cursor = mydb.cursor()


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}


# GET ALL STUDENTS ENDPOINT
@app.get("/students", status_code=status.HTTP_200_OK)
def getAllStudents():
    query = "SELECT * FROM student"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return []


# CREATE A NEW STUDENT ENDPOINT USING QUERY PARAMS
@app.post("/student/create", status_code=status.HTTP_201_CREATED)
def createStudent(
        firstName: str = Query(...),
        lastName: str = Query(...),
        sex: str = Query(...),
        age: int = Query(...),
        phoneNumber: int = Query(...),
        disabled: bool = Query(...),
        department: str = Query(...),
        current_term: str = Query(...)
):
    query = """
    INSERT INTO student (firstName, lastName, sex, age, phoneNumber, disabled, department, current_term) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    student_data = (
        firstName,
        lastName,
        sex,
        age,
        phoneNumber,
        disabled,
        department,
        current_term
    )

    cursor.execute(query, student_data)
    mydb.commit()

    return {
        "id": cursor.lastrowid,
        "firstName": firstName,
        "lastName": lastName,
        "sex": sex,
        "age": age,
        "phoneNumber": phoneNumber,
        "disabled": disabled,
        "department": department,
        "current_term": current_term
    }
