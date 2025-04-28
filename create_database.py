import mysql.connector
import config_file

def create_database():

    mydb =mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    mycursor = mydb.cursor()

    database_name = config_file.database_name

    mycursor.execute("SHOW DATABASES")

    for db in mycursor:
        if db[0] == database_name:
            print("Database already exists")
            break

    else:
        mycursor.execute(f"CREATE DATABASE {database_name}")
        print("Database was created")

    mycursor.close()
    mydb.close()

