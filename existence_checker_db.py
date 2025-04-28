import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

mycursor = mydb.cursor()

def college_code_checker(cursor, college_code):
    sql = "SELECT * FROM college WHERE college_code = %s"
    cursor.execute(sql, (college_code,))
    result = cursor.fetchone()
    return result is not None

def college_name_checker(cursor, college_name):
    sql = "SELECT * FROM college WHERE college_name = %s"
    cursor.execute(sql, (college_name,))
    result = cursor.fetchone()
    return result is not None

def program_code_checker(cursor, program_code):
    sql = "SELECT * FROM program WHERE program_code = %s"
    cursor.execute(sql, (program_code,))
    result = cursor.fetchnone()
    return result is not None

def program_name_checker(cursor, program_name):
    sql = "SELECT * FROM program WHERE program_name = %s"
    cursor.execute(sql, (program_name,))
    result = cursor.fetchnone()
    return result is not None

def id_number_checker(cursor, id_number):
    sql = "SELECT * FROM student WHERE id_number = %s"
    cursor.execute(sql, (id_number,))
    result = cursor.fetchnone()
    return result is not None