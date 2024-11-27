from fastapi import FastAPI, HTTPException, status, Query

from sqlalchemy import create_engine, text


app = FastAPI()

# Connect to the database
host = "localhost"
username = "root"
password = ""
database = "fast_api_school"


# CREATED THE ENGINE TO ESTABLISH A CONNECTION WITH THE MYSQL DB
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}", echo=True)


with engine.connect() as conn:
    result = conn.execute(text("select 'hello world' "))
    print(result.all())




# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}


# GET ALL STUDENTS ENDPOINT

