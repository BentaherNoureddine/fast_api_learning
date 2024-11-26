import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fast_api_school"
)

# Create a cursor object
# the cursor is used to execute sql queries
cursor = mydb.cursor()
