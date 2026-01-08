import mysql.connector as mc

con = mc.connect(
    host="localhost",
    user="root",
    password="akash903",
    database="coe"
)
print("Database connection successfully")
