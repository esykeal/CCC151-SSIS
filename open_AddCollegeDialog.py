from PyQt6.QtWidgets import QDialog, QMessageBox
from AddDialog_folder.AddCollege_Dialog_ui import Ui_AddCollege_Dialog
import mysql.connector
from db_connection import get_connection
from existence_checker_db import college_code_checker, college_name_checker

class AddCollegeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddCollege_Dialog()
        self.ui.setupUi(self)

        mydb = get_connection()
        mycursor = mydb.cursor()

        #When Save and Cancel button is clicked, call respective functions
        self.ui.Save_button.clicked.connect(self.save_college)
        self.ui.Cancel_button.clicked.connect(self.cancel_action)

    #Funtion to cancel/close the dialog
    def cancel_action(self):
        print("Adding College cancelled")
        self.reject()

    #Function to save college to csv
    def save_college(self):
        college_code = self.ui.CollegeCode_input.text()
        college_name = self.ui.CollegeName_input.text()

        if college_code_checker(self.cursor, college_code):
            QMessageBox.warning(self, "Error", "College code already exists!")
            return
        if college_name_checker(self.cursor, college_name):
            QMessageBox.warning(self, "Error", "College name already exists!")
            return
        if not college_code:
            QMessageBox.warning(self,"Error","Field can't be empty")
            return
        if not college_name:
            QMessageBox.warning(self,"Error","Field can't be empty")
            return
        else:
            insert_college_sql = "INSERT INTO college(college_code, college_name) VALUES (%s, %s)"
            values = (college_code, college_name)

            try:
                self.mycursor.execute(insert_college_sql, values)
                self.mydb.commit()
                QMessageBox.information(self, "Success", "College added successfully!")
                self.accept()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.mydb.rollback()  # Rollback if there's an error
                QMessageBox.critical(self, "Error", "An error occurred while adding the college.")

        #TODO: LOAD THE DATA IN THE GUI, SORT IT IF IT HAS A SORT, ACCEPT IT
        self.parent().show_college_db_to_table()
        self.parent().sort_table()