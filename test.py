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


def sort_table():
    current_index = self.ui.stackedWidget.currentIndex()

    #If the current index is 2, then its the college table
    if current_index == 2:
        table_widget = self.college_table
        table_type = "COLLEGES"
        sort_combo = self.ui.comboBox_3
        sort_mapping_sql = {
                1: "ORDER BY college_code ASC", # College Code (A-Z)
                2: "ORDER BY college_code DESC", # College Code Z-A
                3: "ORDER BY college_name ASC",  #College Name (A-Z)
                4: "ORDER BY college_name DESC", # College Z-A
            }
        
    if current_index == 1:
        table_widget = self.program_table
        table_type = "PROGRAMS"
        sort_combo = self.ui.comboBox_2
        sort_mapping_sql = {
            1: "ORDER BY program_code ASC", #Program Code (A-Z)
            2: "ORDER BY program_code DESC", #Program Code (Z-A)
            3: "ORDER BY program_name ASC",  #Program Name (A-Z)
            4: "ORDER BY program_name DESC", #Program Name (Z-A)
            5: "ORDER BY college_code ASC", #College Code (A-Z)
            6: "ORDER BY college_code DESC" #College code (Z-A)
            }
        
    if current_index == 0:
            table_widget = self.student_table
            table_type = "STUDENTS"
            sort_combo = self.ui.comboBox
            sort_mapping_sql = {
                1: "ORDER BY first_name ASC",  # First Name (A-Z)
                2: "ORDER BY first_name DESC",  # First Name (Z-A)
                3: "ORDER BY last_name ASC",  # Last Name (A-Z)
                4: "ORDER BY last_name DESC",  # Last Name (Z-A)
                5: "ORDER BY id_number ASC",  # Student ID (Ascending)
                6: "order by id_number DESC",  # Student ID (Descending)
                7: "ORDER BY year_level ASC",  # Year Level (1-4)
                8: "ORDER BY year_level DESC",  # Year Level (4-1)
                9: "ORDER BY program_code ASC",  # Program Code (A-Z)
                10: "ORDER BY gender ASC" # Gender
            }