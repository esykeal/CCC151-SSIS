import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "root"
)

#Code belows is a way to see if the database connected
#print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    if ("name") not in x:
        mycursor.execute("CREATE DATABASE name")
