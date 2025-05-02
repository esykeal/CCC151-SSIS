from db_connection import get_connection
import mysql.connector

mydb = get_connection()
mycursor = mydb.cursor()

def college_code_checker(cursor, college_code):
    sql = "SELECT college_code FROM college WHERE college_code = %s"
    cursor.execute(sql, (college_code,))
    result = cursor.fetchone()
    return result is not None

def college_name_checker(cursor, college_name):
    sql = "SELECT college_name FROM college WHERE college_name = %s"
    cursor.execute(sql, (college_name,))
    result = cursor.fetchone()
    return result is not None

def program_code_checker(cursor, program_code):
    sql = "SELECT program_code FROM program WHERE program_code = %s"
    cursor.execute(sql, (program_code,))
    result = cursor.fetchone()
    return result is not None

def program_name_checker(cursor, program_name):
    sql = "SELECT program_name FROM program WHERE program_name = %s"
    cursor.execute(sql, (program_name,))
    result = cursor.fetchone()
    return result is not None

def id_number_checker(cursor, id_number):
    sql = "SELECT id_number FROM student WHERE id_number = %s"
    cursor.execute(sql, (id_number,))
    result = cursor.fetchone()
    return result is not None