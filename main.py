import sys
import os

import create_database
from existence_checker_db import college_code_checker, college_name_checker, program_code_checker, program_name_checker, id_number_checker

from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidget , QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox
from PyQt6 import QtWidgets, QtCore
from AddDialog_folder.AddStudent_Dialog_ui import Ui_AddStudent_Dialog
from AddDialog_folder.AddProgram_Dialog_ui import Ui_AddProgram_Dialog
from AddDialog_folder.AddCollege_Dialog_ui import Ui_AddCollege_Dialog

from EditDialog_folder.EditStudent_Dialog import Ui_EditStudent_Dialog
from EditDialog_folder.EditProgram_Dialog import Ui_EditProgram_Dialog
from EditDialog_folder.EditCollege_Dialog import Ui_EditCollege_Dialog

from deleteItemConfirmation import Ui_DeleteConfirmation

from final2 import Ui_MainWindow

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="your_database_name"
)

#Creates the database if its not created yet
create_database.create_database()

#Opens the Add College Dialog when button is clicked
class AddCollegeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddCollege_Dialog()
        self.ui.setupUi(self)

        #When Save and Cancel button is clicked, call respective functions
        self.ui.Save_button.clicked.connect(self.save_college)
        self.ui.Cancel_button.clicked.connect(self.cancel_action)

    #Funtion to cancel/close the dialog
    def cancel_action(self):
        print("College Dialog Cancelled")
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

        if not college_name:
            QMessageBox.warning(self,"Error","Field can't be empty")

        else:
            insert_college_sql = "INSERT INTO college(college_code, college_name) VALUES (%s, %s)"
            values = (college_code, college_name)

            try:
                self.cursor.execute(insert_college_code_sql, values)
                self.db.commit()
                QMessageBox.information(self, "Success", "College added successfully!")
                self.accept()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.db.rollback()  # Rollback if there's an error
                QMessageBox.critical(self, "Error", "An error occurred while adding the college.")

        #TODO: LOAD THE DATA IN THE GUI, SORT IT IF IT HAS A SORT, ACCEPT IT
        
        #Reloads the table to show the added college
        self.parent().load_csv_to_table(self.parent().college_table, csv_filename, "COLLEGES")
        self.parent().sort_table()
        self.accept()

#Opens the Add Program Dialog when button is clicked
class AddProgramDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProgram_Dialog()
        self.ui.setupUi(self)

        #When Save and Cancel button is clicked, call respective funtions
        self.ui.Save_button.clicked.connect(self.save_program)
        self.ui.Cancel_button.clicked.connect(self.cancel_action)

    #Funtion to cancel/close the dialog
    def cancel_action(self):
        print("Program Dialog Cancelled") #Optional
        self.reject()

    #Function to save program to csv
    def save_program(self):
        program_code = self.ui.ProgramCode_input.text()
        program_name = self.ui.ProgramName_input.text()
        college_code = self.ui.CollegeCode_input.text()
        
        if program_code_checker(self.cursor, program_code):
            QMessageBox.warning(self, "Error", "Program Code already exists!")
            return
        
        if program_name_checker(self.cursor, program_name):
            QMessageBox.warning(self, "Error", "Program Name already exists!")
            return

        if not college_code_checker(self.cursor, college_code):
            QMessageBox.warning(self, "Error", "College code doesn't exists")
            return

        if not program_code:
            QMessageBox.warning(self,"Error","Field can't be empty")
        if not program_name:
            QMessageBox.warning(self,"Error","Field can't be empty")
        if not college_code:
            QMessageBox.warning(self,"Error","Field can't be empty") 
        
        else:
            insert_program_sql = "INSERT INTO program(program_code, program_name, college_code) VALUES (%s, %s, %s)"
            values = (program_code, program_name, college_code)

            try:
                self.cursor.execute(insert_program_sql, values)
                self.db.commit()
                QMessageBox.information(self, "Success", "Program added successfully!")
                self.accept()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.db.rollback()  # Rollback if there's an error
                QMessageBox.critical(self, "Error", "An error occurred while adding the program.")

        #TODO: LOAD IT TO THE GUI, SORT IT IF NAKA SORT, THEN CLOSE
        self.parent().load_csv_to_table(self.parent().program_table, csv_filename, "PROGRAMS")
        self.parent().sort_table()
        self.accept()

#Opens the Add Student Dialog when button is clicked
class AddStudentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddStudent_Dialog()
        self.ui.setupUi(self)

        #When Save and Cancel button is clicked, call respective funtions
        self.ui.Save_button.clicked.connect(self.save_student)
        self.ui.Cancel_button.clicked.connect(self.cancel_action)

    #Funtion to cancel/close the dialog
    def cancel_action(self):
        print("Student Dialog Cancelled") #Optional
        self.reject()

    #Function to save student to csv
    def save_student(self):
        id_number = self.ui.ID_Number_input.text()
        first_name = self.ui.First_Name_input.text()
        last_name = self.ui.Last_Name_input.text()
        gender = self.ui.Gender_input.text()
        year_level = self.ui.Year_Level_comboBox.currentText()
        program_code = self.ui.Program_Code_input.text()

        if not program_code_checker(self.cursor, program_code):
            QMessageBox.warning(self, "Error", "Program Code doesn't exists!")
            return

        if id_number_checker(self.cursor, id_number):
            QMessageBox.warning(self, "Error", "ID Number already exists")
            return

        if not all([id_number, first_name, last_name, year_level, gender, program_code]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
            return
                
        else:
            insert_student_sql = "INSERT INTO student(id_number, first_name, last_name, gender, year_level, program_code) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (id_number, first_name, last_name, gender, year_level, program_code)

            try:
                self.cursor.execute(insert_student_sql, values)
                self.db.commit()
                QMessageBox.information(self, "Success", "Student added successfully!")
                self.accept()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.db.rollback()  # Rollback if there's an error
                QMessageBox.critical(self, "Error", "An error occurred while adding the student.")


        #TODO: LOAD THIS DATA TO THE CSV, SORT IF IF NAAY SORT
        self.parent().load_csv_to_table(self.parent().student_table, csv_filename, "STUDENTS")
        self.parent().sort_table()
        self.accept()

#Opens a Edit Dialog when edit button is clicked
class EditStudentDialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = Ui_EditStudent_Dialog()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent

        self.original_row = row_data.copy()

        self.ui.ID_Number_input.setText(row_data[0])
        self.ui.First_Name_input.setText(row_data[1])
        self.ui.Last_Name_input.setText(row_data[2])
        self.ui.Year_Level_comboBox.setCurrentText(row_data[3])
        self.ui.Gender_input.setText(row_data[4])
        self.ui.Program_Code_input.setText(row_data[5])

        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        updated_row = [
            self.ui.ID_Number_input.text(),
            self.ui.First_Name_input.text(),
            self.ui.Last_Name_input.text(),
            self.ui.Year_Level_comboBox.currentText(),
            self.ui.Gender_input.text(),
            self.ui.Program_Code_input.text()
        ]

        if updated_row == self.original_row:
            self.reject()  # Close dialog without saving
            return

        if idNumber_existence(config_file.student_filename, self.ui.ID_Number_input.text()):
            QMessageBox.warning(self, "Error", "ID Number already exists")
            return

        if updated_row != self.original_row:
            if any(field == "" for field in updated_row):
                QMessageBox.warning(self, "Input Error", "Fields can't be empty")
                return
        else:
            self.reject()  # Close dialog without saving
            return


        filename = config_file.student_filename

        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        if 1 <= self.row_index < len(data):
            data[self.row_index] = updated_row

        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        print("✅ Student data updated successfully.")

        self.parent.load_csv_to_table(self.parent.student_table, filename, "STUDENTS")

        self.accept()

#Opens a Edit Dialog when edit button is clicked
class EditCollegeDialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = Ui_EditCollege_Dialog()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent
        self.old_college_code = row_data[0]
        self.old_college_name = row_data[1]

        #Filling data input
        self.ui.CollegeCode_input.setText(row_data[0]) 
        self.ui.CollegeName_input.setText(row_data[1])

        #Calling functions when button is pressed
        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        #The input will become the new data
        new_college_code = self.ui.CollegeCode_input.text().strip()
        new_college_name = self.ui.CollegeName_input.text().strip()

        if new_college_code == self.old_college_code:
            pass
        else:
            if collegeCode_existence(config_file.college_filename, new_college_code):
                QMessageBox.warning(self, "Error", "College code already exists!")
                return
            
        if new_college_name == self.old_college_name:
            pass
        else:
            if collegeName_existence(config_file.college_filename, new_college_name):
                QMessageBox.warning(self, "Error", "College already exists!")
                return

        if not new_college_code:
            QMessageBox.warning(self, "Error", "College code cannot be empty!")
            return

        if not new_college_name:
            QMessageBox.warning(self, "Error", "College cannot be empty!")
            return
        
        filename = config_file.college_filename

        # Read the existing data
        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        # Update the row in `college.csv`
        if 1 <= self.row_index < len(data):
            data[self.row_index] = [new_college_code, new_college_name]

        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        # Check if college code was changed and update `program.csv`
        if new_college_code != self.old_college_code:
            self.update_program_college_codes(self.old_college_code, new_college_code)
            self.parent.load_csv_to_table(self.parent.program_table, config_file.program_filename, "PROGRAMS")

        print("✅ College data updated successfully.")

        self.parent.load_csv_to_table(self.parent.program_table, config_file.program_filename, "PROGRAMS")
        self.parent.load_csv_to_table(self.parent.college_table, config_file.college_filename, "COLLEGES")
        
        self.accept()

    def update_program_college_codes(self, old_code, new_code):
        """Update the college code in program.csv when a college code is changed."""
        program_filename = config_file.program_filename
        updated_data = []

        with open(program_filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        # Ensure data is not empty
        if not data:
            print("⚠️ Warning: program.csv is empty or missing headers.")
            return

        # Check if the file has a header
        header = data[0] if len(data) > 0 else None
        rows = data[1:]  if len(data) > 1 else []# Exclude header

        print(f"📄 Loaded {len(rows)} rows from program.csv")


        for row in rows:
            if len(row) < 3:  # Ensure the row has at least 3 columns
                print(f"⚠ Skipping invalid row: {row}")
                continue  # Skip this row to prevent IndexError

            original_code = row[2].strip()
            print(f"🔎 Checking row: {row}")

            if original_code == old_code:  # Check the correct column
                print(f"📝 Updating: {original_code} → {new_code}")
                row[2] = new_code
                
            updated_data.append(row)

        if not updated_data:
            print("❌ No updates made to program.csv")
            return
        
        # Write back to program.csv
        with open(program_filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            if header:
                csv_writer.writerow(header)  # Keep the header row

            csv_writer.writerows(updated_data)

        print(f"✅ Successfully updated {old_code} → {new_code} in program.csv")

#Opens a Edit Dialog when edit button is clicked
class EditProgramDialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = Ui_EditProgram_Dialog()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent
        self.old_program_code = row_data[0]
        self.old_program_name = row_data[1]
        self.old_college_code = row_data[2]

        #Fill data input
        self.ui.ProgramCode_input.setText(row_data[0])
        self.ui.ProgramName_input.setText(row_data[1])
        self.ui.CollegeCode_input.setText(row_data[2])

        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        #The input will become the new data

        new_program_code = self.ui.ProgramCode_input.text().strip()
        new_program_name = self.ui.ProgramName_input.text().strip()
        new_college_code = self.ui.CollegeCode_input.text().strip()
        
        if [new_program_code, new_program_name, new_college_code] == [self.old_program_code, self.old_program_name, self.old_college_code]:
            self.reject()  # No changes made, close dialog without saving
            return

        if new_program_code != self.old_program_code and programCode_existence(config_file.program_filename, new_program_code):
            QMessageBox.warning(self, "Error", "Program code already exists!")
            return
        if new_program_name != self.old_program_name and programName_existence(config_file.program_filename, new_program_name):
            QMessageBox.warning(self, "Error", "Program name already exists!")
            return
        
        if any(field == "" for field in [new_program_code, new_program_name, new_college_code]):
            QMessageBox.warning(self, "Error", "Fields can't be empty")
            return
        
        if not collegeCode_existence(config_file.college_filename, new_college_code):
            QMessageBox.warning(self, "Error", "College code doesn't exist")
            return

        filename = config_file.program_filename

        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        if 1 <= self.row_index < len(data):
            data[self.row_index] = [new_program_code, new_program_name, new_college_code]

        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        if new_program_code != self.old_program_code:
            self.update_student_program_codes(self.old_program_code, new_program_code)
            self.parent.load_csv_to_table(self.parent.student_table, config_file.student_filename, "STUDENTS")

        print(" ✅Program data updated succesfully.")

        self.parent.load_csv_to_table(self.parent.student_table, config_file.student_filename, "STUDENTS")
        self.parent.load_csv_to_table(self.parent.program_table, config_file.program_filename, "PROGRAMS")

        self.accept()

    def update_student_program_codes(self, old_code, new_code):
        student_filename = config_file.student_filename
        updated_data = []

        with open(student_filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        if not data:
            print("⚠️ Warning: student.csv is empty or missing headers")
            return
        
        header = data[0] if len(data) > 0 else None
        rows = data[1:]  if len(data) > 1 else []

        print(f"📄 Loaded {len(rows)} rows from program.csv")       

        for row in rows:
            if len(row) < 6:
                print(f"⚠ Skipping invalid row: {row}")
                continue

            original_code = row[5].strip()
            print(f"🔎 Checking row: {row}")

            if original_code == old_code:  # Check the correct column
                print(f"📝 Updating: {original_code} → {new_code}")
                row[5] = new_code

            updated_data.append(row)

        if not updated_data:
            print("❌ No updated made to studentInfo.csv")
            return
        
        with open(student_filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            if header:
                csv_writer.writerow(header)

            csv_writer.writerows(updated_data)

        print(f"✅ Successfully updated {old_code} → {new_code} in studentInfo.csv")

#Opens a delete confirmation dialog when delete button is clicked
class DeleteItemConfirmation(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteConfirmation()
        self.ui.setupUi(self)

        self.ui.Confirm.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Aron dli ma click
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        #self.ui.tableWidget.setEnabled(False)

        #Function call for using search function
        self.ui.search_text.textChanged.connect(self.search_table)

        #nicknames for the tan;es
        self.student_table = self.ui.tableWidget
        self.program_table = self.ui.tableWidget_2
        self.college_table = self.ui.tableWidget_3

        #Set the table to stretch the columns per table
        self.student_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.program_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.college_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        #Lets you only see the sidebar with the icons only
        self.ui.sidebar_icon_with_description_widget.hide()

        #Add functionality to the exit buttons
        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.ui.exit_icon_only.clicked.connect(QApplication.instance().quit)

        #Add functionality to the sidebar buttons
        self.ui.students_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.programs_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.colleges_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.students_icon_only.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.programs_icon_only.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.college_icon_only.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        #When add [student, program, college] button is clicked, open the respective dialog
        self.ui.addstudent_button.clicked.connect(self.open_add_student_dialog)
        self.ui.addprogram_button.clicked.connect(self.open_add_program_dialog)
        self.ui.addcollege_button.clicked.connect(self.open_add_college_dialog)

        #MAYBE USEFUL FOR UPDATING
        #Load the CSV files to the table
        self.load_csv_to_table(self.student_table, config_file.student_filename, "STUDENTS")
        self.load_csv_to_table(self.program_table, config_file.program_filename, "PROGRAMS")
        self.load_csv_to_table(self.college_table, config_file.college_filename, "COLLEGES")

        #SORTING
        self.ui.comboBox.currentIndexChanged.connect(self.sort_table)
        self.ui.comboBox_2.currentIndexChanged.connect(self.sort_table)
        self.ui.comboBox_3.currentIndexChanged.connect(self.sort_table)
        
    #Function to call [student, program, and college] dialog when the button is clicked
    def open_add_student_dialog(self):
        dialog = AddStudentDialog(self)
        dialog.exec()
    def open_add_program_dialog(self):
        dialog = AddProgramDialog(self)
        dialog.exec()
    def open_add_college_dialog(self):
        dialog = AddCollegeDialog(self)
        dialog.exec()

    #Function to load the csv files to the tables
    def load_csv_to_table(self, table_widget, filename, table_type):
        if not os.path.isfile(filename):
            print(f" File {filename} does not exist yet.")
            return

        with open(filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

            if not data:
                print(f" {filename} is empty.")
                return
            
            #Get headers from config_file.py
            headers = config_file.header_names.get(table_type, [])
            fieldnames = [h[0] for h in headers] #Unused yet
            readable_headers = [h[1] for h in headers]

            #Sets the table headers and adds one for the Actions
            table_widget.setHorizontalHeaderLabels(readable_headers + ["Actions"])

            #Adds data to the table
            rows = data[1:]
            table_widget.setRowCount(len(rows))
            for row_index, row in enumerate(rows):
                for col_index, value in enumerate(row):
                    if col_index < table_widget.columnCount() - 1: # Ignore last column for buttons
                        table_widget.setItem(row_index, col_index, QTableWidgetItem(value))

                #Adds buttons to the last column
                action_widget = QWidget()
                layout = QHBoxLayout(action_widget)
                layout.setContentsMargins(0, 0, 0, 0)

                #Edit button stylesheet
                edit_button = QPushButton("Edit")
                edit_button.clicked.connect(lambda _, ri=row_index: self.edit_row(table_widget, filename, ri))
                layout.addWidget(edit_button)

                #Delete button stylesheet
                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda _, ri=row_index: self.confirm_delete_Row(table_widget, filename, ri))
                layout.addWidget(delete_button)
                
                #Puts the button to the column
                table_widget.setCellWidget(row_index, len(readable_headers), action_widget)

            print(f" Loaded {filename} into {table_type} table with custom headers.")
    
    #Function to edit the row
    def edit_row(self, table_widget, filename, row_index):
        print(f"Editing row {row_index} in {filename}")
        
        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list (csv_reader)


        row_index = row_index + 1

        if row_index < 1 or row_index >= len(data):
            print("Invalid row index. Skipping edit.")
            return

        row_data = data[row_index]

        if filename == config_file.student_filename:
            dialog = EditStudentDialog(self, row_data, row_index)
            table_type = "STUDENTS"
        elif filename == config_file.program_filename:
            dialog = EditProgramDialog(self, row_data, row_index)
            table_type = "PROGRAMS"
        elif filename == config_file.college_filename:
            dialog = EditCollegeDialog(self, row_data, row_index)
            table_type = "COLLEGES"
        else:
            print("⚠️ Unknown CSV file. Skipping edit.")
            return
        
        if dialog.exec():  # User clicked Save
            self.load_csv_to_table(table_widget, filename, table_type)

    #Function to delete the row
    def delete_row(self, table_widget, filename, row_index):
        print(f"Deleting row {row_index} from {filename}")

        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        #weirdly ako index ga start sa [1] and not [0], therefore permi ga bug kay akong [1] is my header
        row_index = row_index + 1

        if row_index < 1 or row_index >=len(data):
            print("Invalid row index. Skipping deletion.")
            return

        deleted_row = data[row_index]
        del data[row_index]

        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        table_widget.removeRow(row_index)

        print("Row deleted successfully and CSV updated.")

        if filename == config_file.college_filename:
            #TODO:
            deleted_college_code = deleted_row[0]  # Get deleted college_code
            self.update_programs_after_college_delete(deleted_college_code)

        if filename == config_file.program_filename:
            deleted_program_code = deleted_row[0]
            self.update_students_after_program_delete(deleted_program_code)

        if filename == config_file.student_filename:
            table_type = "STUDENTS"
        elif filename == config_file.program_filename:
            table_type = "PROGRAMS"
        elif filename == config_file.college_filename:
            table_type = "COLLEGES"
        else:
            print("⚠️ Unknown CSV file. Skipping refresh.")
            return  

        self.load_csv_to_table(table_widget, filename, table_type)

    def confirm_delete_Row(self,table_widget, filename, row_index):
        dialog = DeleteItemConfirmation()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            self.delete_row(table_widget, filename, row_index)
        else:
            print("Cancelled")

    #Function for searching
    def search_table(self):
        search_text = self.ui.search_text.text().strip().lower()
        selected_filter = self.ui.SearchFilters.currentIndex()

        print(f"🔎 Search input:'{search_text}'")
        print(f"🔎 Selected filter:'{selected_filter}'")

        current_index = self.ui.stackedWidget.currentIndex()

        if current_index == 0:
            table_widget = self.student_table
            selected_filter = selected_filter - 1
        elif current_index == 1:
            table_widget = self.program_table
            selected_filter = selected_filter - 6
        elif current_index == 2:
            table_widget = self.college_table
            selected_filter = selected_filter - 8
        else:
            print("⚠️ No valid table selected!")
            return
    
        for row in range(table_widget.rowCount()):
            item = table_widget.item(row, selected_filter)
            
            if not search_text:
                table_widget.setRowHidden(row, False)
            else:
                if item and search_text in item.text().strip().lower():
                    table_widget.setRowHidden(row, False)
                else:
                    table_widget.setRowHidden(row, True)

    #Function for sorting the tables
    def sort_table(self):
        current_index = self.ui.stackedWidget.currentIndex()

        if current_index == 0:
            table_widget = self.student_table
            filename = config_file.student_filename
            table_type = "STUDENTS"
            sort_combo = self.ui.comboBox
            sort_mapping = {
                1: (1, QtCore.Qt.SortOrder.AscendingOrder),  # First Name (A-Z)
                2: (1, QtCore.Qt.SortOrder.DescendingOrder),  # First Name (Z-A)
                3: (2, QtCore.Qt.SortOrder.AscendingOrder),  # Last Name (A-Z)
                4: (2, QtCore.Qt.SortOrder.DescendingOrder),  # Last Name (Z-A)
                5: (0, QtCore.Qt.SortOrder.AscendingOrder),  # Student ID (Ascending)
                6: (0, QtCore.Qt.SortOrder.DescendingOrder),  # Student ID (Descending)
                7: (3, QtCore.Qt.SortOrder.AscendingOrder),  # Year Level (1-4)
                8: (3, QtCore.Qt.SortOrder.DescendingOrder),  # Year Level (4-1)
                9: (5, QtCore.Qt.SortOrder.AscendingOrder),  # Program Code (A-Z)
                10: (4, QtCore.Qt.SortOrder.AscendingOrder)  # Gender
            }

        elif current_index == 1:
            table_widget = self.program_table
            filename = config_file.program_filename
            table_type = "PROGRAMS"
            sort_combo = self.ui.comboBox_2
            sort_mapping = {
                1: (0, QtCore.Qt.SortOrder.AscendingOrder), #Program Code (A-Z)
                2: (0, QtCore.Qt.SortOrder.DescendingOrder), #Z-A
                3: (1, QtCore.Qt.SortOrder.AscendingOrder),  #Program Name (A-Z)
                4: (1, QtCore.Qt.SortOrder.DescendingOrder), #Z-A
                5: (2, QtCore.Qt.SortOrder.AscendingOrder), #College Code (A-Z)
                6: (2, QtCore.Qt.SortOrder.DescendingOrder) #Z-A
            }
        elif current_index == 2:
            table_widget = self.college_table
            filename = config_file.college_filename
            table_type = "COLLEGES"
            sort_combo = self.ui.comboBox_3
            sort_mapping = {
                1: (0, QtCore.Qt.SortOrder.AscendingOrder), #College Code (A-Z)
                2: (0, QtCore.Qt.SortOrder.DescendingOrder), #Z-A
                3: (1, QtCore.Qt.SortOrder.AscendingOrder),  #College Name (A-Z)
                4: (1, QtCore.Qt.SortOrder.DescendingOrder), #Z-A
            }
        else:
            print("⚠️ No active table found.")
            return

        selected_sort_index = sort_combo.currentIndex()

        if selected_sort_index not in sort_mapping:
            print(f"🔄 Restoring {table_type} Table to Original Order from CSV...")
            self.load_csv_to_table(table_widget, filename, table_type)
            return
        
        column_index, sort_order = sort_mapping[selected_sort_index]

        print(f"🔄 Sorting {table_type} Table by Column Index: {selected_sort_index}")

        table_widget.sortItems(column_index, sort_order)

    def update_programs_after_college_delete(self, deleted_college_code):
        program_filename = config_file.program_filename
        updated_data = []

        with open(program_filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)

        if not data:
            print("⚠️ Warning: program.csv is empty or missing headers.")
            return
    
        header = data[0]
        rows = data[1:]

        for row in rows:
            if row[2] == deleted_college_code:
                print(f"🔄 Updating program {row[0]} (was under {deleted_college_code}) to 'N/A'")
                row[2] = "N/A"  # Replace college_code with "N/A"
            updated_data.append(row)

        with open(program_filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(updated_data)

        print(f"✅ Programs under {deleted_college_code} updated to 'N/A'.")
        self.load_csv_to_table(self.program_table, program_filename, "PROGRAMS")

        self.update_students_after_program_delete("N/A")

    def update_students_after_program_delete(self, deleted_program_code):
        student_filename = config_file.student_filename
        updated_data = []

        with open(student_filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)

        if not data:
            print("⚠️ Warning: student.csv is empty or missing headers.")
            return

        header = data[0]
        rows = data[1:]

        for row in rows:
            if row[5] == deleted_program_code:  # If program_code matches deleted program
                print(f"🔄 Updating student {row[0]} (was in {deleted_program_code}) to 'Unenrolled'")
                row[5] = "Unenrolled"  # Replace program_code with "Unenrolled"
            updated_data.append(row)

        with open(student_filename, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            csv_writer.writerows(updated_data)

        print(f"✅ Students under {deleted_program_code} updated to 'Unenrolled'.")
        self.load_csv_to_table(self.student_table, student_filename, "STUDENTS")

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec())