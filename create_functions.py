import mysql.connector
import config
from mysql.connector import Error
from db_connection import get_connection

def create_database():
    try:
        mydb =mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        mycursor = mydb.cursor()

        database_name = config.database_name

        mycursor.execute("SHOW DATABASES")

        databases = mycursor.fetchall()

        for db in databases:
            if db[0] == database_name:
                print("Database already exists")
                break

        else:
            mycursor.execute(f"CREATE DATABASE {database_name}")
            print("Database was created")
    
    except Error as err:
        print(f"Error: {err}")
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

    mycursor.close()
    mydb.close()

def create_college_table():
    try:
        mydb = get_connection()
        mycursor = mydb.cursor()

        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS college (
                college_code VARCHAR(10),
                college_name VARCHAR(50) NOT NULL UNIQUE,
                PRIMARY KEY (college_code)
                );
        """)
        print("College table created successfully")

        mycursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def create_program_table():
    try:
        mydb = get_connection()
        mycursor = mydb.cursor()

        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS program (
                program_code VARCHAR(10),
                program_name VARCHAR(50) NOT NULL UNIQUE,
                college_code VARCHAR(10) NULL,
                FOREIGN KEY (college_code) 
                    REFERENCES college(college_code)
                    ON DELETE SET NULL,
                    ON UPDATE CASCADE
                PRIMARY KEY (program_code)
            );
        """)
        print("Program table created successfully")

        mycursor.close()
        mydb.close()
    except mysql.connector.Error as err:
            print(f"Error: {err}")

def create_student_table():
    try:
        mydb = get_connection()
        mycursor = mydb.cursor()

        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS student(
                id_number VARCHAR(9),
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                gender VARCHAR(6) NOT NULL,
                year_level INT NOT NULL,
                program_code VARCHAR(10) NULL,
                FOREIGN KEY (program_code) 
                    REFERENCES program(program_code)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL,
                PRIMARY KEY (id_number)
                );
        """)
        print("Student table created successfully")
        mycursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")