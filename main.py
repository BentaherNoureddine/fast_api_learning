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

# USING engine.connect() to make transactions
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world' "))
    print(result.all())

# USING the powerful engine.begin() to make transaction
with engine.begin() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
    )


# ROOT ENDPOINT
@app.get("/")
def read_root():
    return {"HELLO FAST API STUDENTS"}

# GET ALL STUDENTS ENDPOINT
