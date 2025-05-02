import sys
import mysql.connector
import config

from db_connection import get_connection

from create_functions import *

from existence_checker_db import *

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton, QLineEdit
from PyQt6 import QtWidgets

from main_gui import Ui_MainWindow

from rev_AddDialog_folder.rev_AddCollegeDialog_ui import Ui_Add_College_Dialog
from rev_AddDialog_folder.rev_AddProgramDialog_ui import Ui_Add_Program_Dialog
from rev_AddDialog_folder.rev_AddStudentDialog_ui import Ui_Add_Student_Dialog

from rev_EditDialog_folder.rev_EditCollegeDialog_ui import Ui_Edit_College_Dialog
from rev_EditDialog_folder.rev_EditProgramDialog_ui import Ui_Edit_Program_Dialog
from rev_EditDialog_folder.rev_EditStudentDialog_ui import Ui_Edit_Student_Dialog

create_database()
create_college_table()
create_program_table()
create_student_table()

class AddCollege_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Add_College_Dialog()
        self.ui.setupUi(self)

        self.setStyleSheet("")

        with open("styles/add_college_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()

        self.ui.Save_button.clicked.connect(self.save_college)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_college(self):
        college_code = self.ui.CollegeCode_input.text()
        college_name = self.ui.CollegeName_input.text()

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            if college_code_checker(mycursor, college_code):
                QMessageBox.warning(self, "Error", "College code already exists")
                return
            
            if college_name_checker(mycursor, college_name):
                QMessageBox.warning(self, "Error", "College name already exists")
                return
                
            if not college_code and not college_name:
                QMessageBox.warning(self, "Error", "All fields must be filled")
                return

            sql = "INSERT INTO college (college_code, college_name) VALUES (%s, %s)"
            mycursor.execute(sql, (college_code, college_name))
            mydb.commit()

            print(f"{college_code} {college_name}")

            QMessageBox.information(self, "Success", "College added successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class AddProgram_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Add_Program_Dialog()
        self.ui.setupUi(self)

        self.load_college_code()

        self.setStyleSheet("")

        with open("styles/add_program_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()

        self.ui.Save_button.clicked.connect(self.save_program)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def load_college_code(self):
        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            sql = "SELECT college_code FROM college"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            self.ui.college_code_input_comboBox.clear()
            for row in result:
                college_code = row[0]
                if college_code:
                    self.ui.college_code_input_comboBox.addItem(college_code)
        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))
            
        finally:
            if mycursor:
                mycursor.close()
            if mydb:
                mydb.close()

    def save_program(self):
        program_code = self.ui.ProgramCode_input.text()
        program_name = self.ui.ProgramName_input.text()
        college_code = self.ui.college_code_input_comboBox.currentText()

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            if program_code_checker(mycursor, program_code):
                QMessageBox.warning(self, "Error", "Program code already exists")
                return
            if program_name_checker(mycursor, program_name):
                QMessageBox.warning(self, "Error", "Program name already exists")
                return
            if not program_code or not program_name or not college_code:
                QMessageBox.warning(self, "Error", "All fields must be filled in")
                return
        
            sql = "INSERT INTO program (program_code, program_name, college_code) VALUES (%s, %s, %s)"
            mycursor.execute(sql, (program_code, program_name, college_code))
            mydb.commit()

            QMessageBox.information(self, "Success", "Program added successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class AddStudent_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = Ui_Add_Student_Dialog()
        self.ui.setupUi(self)

        self.load_program_code()

        self.setStyleSheet("")

        with open("styles/add_student_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()

        self.ui.Save_button.clicked.connect(self.save_student)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def load_program_code(self):
        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            sql = "SELECT program_code FROM program"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            self.ui.program_code_input_comboBox.clear()
            for row in result:
                program_code = row[0]
                if program_code:
                    self.ui.program_code_input_comboBox.addItem(program_code)

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

        finally:
            if mycursor:
                mycursor.close()
            if mydb:
                mydb.close()

    def save_student(self):
        id_number = self.ui.id_number_input.text()
        first_name = self.ui.first_name_input.text()
        last_name = self.ui.last_name_input.text()
        gender = self.ui.gender_comboBox.currentText()
        year_level = self.ui.year_level_comboBox.currentText()
        program_code = self.ui.program_code_input_comboBox.currentText()

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            if id_number_checker(mycursor, id_number):
                QMessageBox.warning(self, "Error", "ID Number already exists")
                return

            if not all([id_number, first_name, last_name, gender, year_level, program_code]):
                QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
                return
        
            sql = "INSERT INTO student (id_number, first_name, last_name, gender, year_level, program_code) VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, (id_number, first_name, last_name, gender, year_level, program_code))
            mydb.commit()

            QMessageBox.information(self, "Success", "Student added successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class EditCollege_Dialog(QDialog):
    def __init__(self, parent, row_data):
        super().__init__(parent)
        self.parent = parent
        self.row_data = row_data

        self.old_college_code = row_data[0]
        self.old_college_name = row_data[1]

        self.ui = Ui_Edit_College_Dialog()
        self.ui.setupUi(self)

        self.setStyleSheet("")

        with open("styles/edit_college_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()
        
        self.ui.college_code_input.setText(row_data[0])
        self.ui.college_name_input.setText(row_data[1])

        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        new_college_code = self.ui.college_code_input.text()
        new_college_name = self.ui.college_name_input.text()

        try:

            mydb = get_connection()
            mycursor = mydb.cursor()

            if not new_college_code or not new_college_name:
                QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
                return
        
            if new_college_code == self.old_college_code:
                pass
            else:
                if college_code_checker(mycursor, new_college_code):
                    QMessageBox.warning(self, "Error", "College code already exists!")
                    return
                
            if new_college_name == self.old_college_name:
                pass
            else:
                if college_name_checker(mycursor, new_college_name):
                    QMessageBox.warning(self, "Error", "College already exists!")
                    return
                
            sql = "UPDATE college SET college_code = %s, college_name = %s WHERE college_code = %s"
            mycursor.execute(sql, (new_college_code, new_college_name, self.old_college_code))
            mydb.commit()

            QMessageBox.information(self, "Success", "College updated successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class EditProgram_Dialog(QDialog):
    def __init__(self, parent, row_data):
        super().__init__(parent)
        self.parent = parent
        self.row_data = row_data
        
        self.old_program_code = row_data[0]
        self.old_program_name = row_data[1]
        self.old_college_code = row_data[2]

        self.ui = Ui_Edit_Program_Dialog()
        self.ui.setupUi(self)

        self.setStyleSheet("")

        with open("styles/edit_program_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()
        self.retrieve_college_codes()

        self.ui.program_code_input.setText(row_data[0])
        self.ui.program_name_input.setText(row_data[1])
        self.ui.college_code_input_comboBox.setCurrentText(row_data[2])

        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)
        
    def retrieve_college_codes(self):
        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            sql = "SELECT college_code FROM college"
            mycursor.execute(sql)
            college_code = mycursor.fetchall()

            self.ui.college_code_input_comboBox.clear()

            for code in college_code:
                self.ui.college_code_input_comboBox.addItem(code[0])

            index = self.ui.college_code_input_comboBox.findText(self.old_college_code)
            if index >= 0:
                self.ui.college_code_input_comboBox.setCurrentIndex(index)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def save_changes(self):
        new_program_code = self.ui.program_code_input.text()
        new_program_name = self.ui.program_name_input.text()
        new_college_code = self.ui.college_code_input_comboBox.currentText()

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            if not new_program_code or not new_program_name:
                QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
                return
            
            if new_program_code == self.old_program_code:
                pass
            else:
                if program_code_checker(mycursor, new_program_code):
                    QMessageBox.warning(self, "Error", "Program code already exists!")
                    return
                
            if new_program_name == self.old_program_name:
                pass
            else:
                if program_name_checker(mycursor, new_program_name):
                    QMessageBox.warning(self, "Error", "Program name already exists!")
                    return
                
            if new_college_code == self.old_college_code:
                pass

            sql = "UPDATE program SET program_code = %s, program_name = %s, college_code = %s WHERE program_code = %s"
            mycursor.execute(sql, (new_program_code, new_program_name, new_college_code, self.old_program_code))
            mydb.commit()

            QMessageBox.information(self, "Success", "Program updated successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class EditStudent_Dialog(QDialog):
    def __init__(self, parent, row_data):
        super().__init__(parent)
        self.parent = parent
        self.row_data = row_data

        self.old_id_number = row_data[0]
        self.old_first_name = row_data[1]
        self.old_last_name = row_data[2]
        self.old_gender = row_data[3]
        self.old_year_level = row_data[4]
        self.old_program_code = row_data[5]

        self.ui = Ui_Edit_Student_Dialog()
        self.ui.setupUi(self)

        self.setStyleSheet("")

        with open("styles/edit_student_dialog.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.parent.load_to_gui()

        self.retrieve_program_code()

        self.ui.id_number_input.setText(row_data[0])
        self.ui.first_name_input.setText(row_data[1])
        self.ui.last_name_input.setText(row_data[2])
        self.ui.gender_comboBox.setCurrentText(row_data[3])
        self.ui.year_level_comboBox.setCurrentText(row_data[4])

        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def retrieve_program_code(self):
        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            sql = "SELECT program_code FROM program"
            mycursor.execute(sql)
            program_code = mycursor.fetchall()

            self.ui.program_code_input_comboBox.clear()

            for code in program_code:
                self.ui.program_code_input_comboBox.addItem(code[0])

            index = self.ui.program_code_input_comboBox.findText(self.old_program_code)
            if index >= 0:
                self.ui.program_code_input_comboBox.setCurrentIndex(index)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def save_changes(self):
        new_id_number = self.ui.id_number_input.text()
        new_first_name = self.ui.first_name_input.text()
        new_last_name = self.ui.last_name_input.text()
        new_gender = self.ui.gender_comboBox.currentText()
        new_year_level = self.ui.year_level_comboBox.currentText()
        new_program_code = self.ui.program_code_input_comboBox.currentText()

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            if not new_id_number or not new_first_name or not new_last_name:
                QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
                return
            
            if new_id_number == self.old_id_number:
                pass
            else:
                if id_number_checker(mycursor, new_id_number):
                    QMessageBox.warning(self, "Error", "ID number already exists!")
                    return
                
            if new_first_name == self.old_first_name:
                pass

            if new_last_name == self.old_last_name:
                pass

            if new_gender == self.old_gender:
                pass

            if new_year_level == self.old_year_level:
                pass

            if new_program_code == self.old_program_code:
                pass

            sql = """
                UPDATE student
                SET id_number = %s, first_name = %s, last_name = %s, gender = %s, year_level = %s, program_code = %s
                WHERE id_number = %s   
                """
            mycursor.execute(sql, (new_id_number, new_first_name, new_last_name, new_gender, new_year_level, new_program_code))
            mydb.commit()

            QMessageBox.information(self, "Success", "Student updated successfully.")
            self.parent.load_to_gui()
            self.accept()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_to_gui()

        #To switch between the stacked widgets
        self.ui.student_pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.student_pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.program_pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.program_pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.college_pushButton.clicked.connect((lambda: self.ui.stackedWidget.setCurrentIndex(2)))
        self.ui.college_pushButton_2.clicked.connect((lambda: self.ui.stackedWidget.setCurrentIndex(2)))

        #functions for the add button
        self.ui.add_student_button.clicked.connect(self.open_add_student_dialog)
        self.ui.add_program_button.clicked.connect(self.open_add_program_dialog)
        self.ui.add_college_button.clicked.connect(self.open_add_college_dialog)

        self.ui.stackedWidget.currentChanged.connect(self.load_to_gui)

        self.ui.stackedWidget.currentChanged.connect(self.default_search_filter)

        self.ui.student_search_input.textChanged.connect(lambda: self.search(0))
        self.ui.program_search_input.textChanged.connect(lambda: self.search(1))
        self.ui.college_search_input.textChanged.connect(lambda: self.search(2))

        self.ui.student_filter_comboBox.currentIndexChanged.connect(lambda: self.search(0))
        self.ui.program_filter_comboBox.currentIndexChanged.connect(lambda: self.search(1))
        self.ui.college_filter_comboBox.currentIndexChanged.connect(lambda: self.search(2))

        self.ui.college_sort_by_comboBox.currentIndexChanged.connect(lambda: self.sort_by(2))
        self.ui.program_sort_by_comboBox.currentIndexChanged.connect(lambda: self.sort_by(1))
        self.ui.student_sort_by_comboBox.currentIndexChanged.connect(lambda: self.sort_by(0))


        #only shows one sidebar
        self.ui.widget_18.hide()

        self.ui.student_table.verticalHeader().setVisible(False)
        self.ui.program_table.verticalHeader().setVisible(False)
        self.ui.college_table.verticalHeader().setVisible(False)

        self.ui.student_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.program_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.college_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
    
    #functions to call the dialogs
    def open_add_student_dialog(self):
        dialog = AddStudent_Dialog(self)
        dialog.exec()

    def open_add_program_dialog(self):
        dialog = AddProgram_Dialog(self)
        dialog.exec()
    
    def open_add_college_dialog(self):
        dialog = AddCollege_Dialog(self)
        dialog.exec()

    def load_to_gui(self):
        mydb = get_connection()
        mycursor = mydb.cursor()

        current_index = self.ui.stackedWidget.currentIndex()
        self.sort_by(current_index)

        # Determine table and SQL based on view
        if current_index == 2:
            tableWidget = self.ui.college_table
            headers = ["College Code", "College Name", "Actions"]
            sql = "SELECT * FROM college"
        elif current_index == 1:
            tableWidget = self.ui.program_table
            headers = ["Program Code", "Program Name", "College Code", "Actions"]
            sql = "SELECT * FROM program"
        elif current_index == 0:
            tableWidget = self.ui.student_table
            headers = ["ID Number", "First Name", "Last Name", "Gender", "Year Level", "Program Code", "Actions"]
            sql = "SELECT * FROM student"
        else:
            return

        # Clear and reset table
        tableWidget.clear()
        tableWidget.setRowCount(0)
        tableWidget.setColumnCount(len(headers))
        tableWidget.setHorizontalHeaderLabels(headers)

        # Fetch data
        mycursor.execute(sql)
        result = mycursor.fetchall()
        tableWidget.setRowCount(len(result))

        # Index of the Actions column
        actions_col = len(headers) - 1

        for row_index, row_data in enumerate(result):
            # Fill in the data columns (excluding "Actions")
            for col_index in range(actions_col):  # up to but not including 'Actions'
                cell_data = row_data[col_index]
                item = QTableWidgetItem(str(cell_data))
                tableWidget.setItem(row_index, col_index, item)

            # Create action buttons (Edit & Delete)
            action_widget = QWidget()
            layout = QHBoxLayout(action_widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(5)

            edit_button = QPushButton("Edit")
            edit_button.setStyleSheet("background-color: #FFD700; font-weight: bold;")
            edit_button.clicked.connect(lambda _, r=row_index: self.edit_row(r, current_index))
            layout.addWidget(edit_button)

            delete_button = QPushButton("Delete")
            delete_button.setStyleSheet("background-color: #FF6347; font-weight: bold;")
            delete_button.clicked.connect(lambda _, r=row_index: self.delete_row(r, current_index))
            layout.addWidget(delete_button)

            action_widget.setLayout(layout)
            tableWidget.setCellWidget(row_index, actions_col, action_widget)

        mycursor.close()
        mydb.close()

    def edit_row(self, row_index, current_index):
        table = None

        if current_index == 2:
            table = self.ui.college_table
            row_data = [
                table.item(row_index, 0).text(),
                table.item(row_index, 1).text()
            ]
            dialog = EditCollege_Dialog(self, row_data)
            dialog.exec()

        if current_index == 1:
            table = self.ui.program_table
            row_data = [
                table.item(row_index, 0).text(),
                table.item(row_index, 1).text(),
                table.item(row_index, 2).text()
            ]
            dialog = EditProgram_Dialog(self, row_data)
            dialog.exec()

        if current_index == 0:
            table = self.ui.student_table
            row_data = [
                table.item(row_index, 0).text(),
                table.item(row_index, 1).text(),
                table.item(row_index, 2).text(),
                table.item(row_index, 3).text(),
                table.item(row_index, 4).text(),
                table.item(row_index, 5).text()
            ]
            dialog = EditStudent_Dialog(self, row_data)
            dialog.exec()

    def delete_row(self, row_index, current_index):
        table = None
        table_name = ""
        code_column_index = 0
        code_column_name = ""
        entity_label = ""

        # Select correct table and code column
        if current_index == 2:
            table = self.ui.college_table
            table_name = "college"
            code_column_name = "college_code"
            entity_label = "College"

        elif current_index == 1:
            table = self.ui.program_table
            table_name = "program"
            code_column_name = "program_code"
            entity_label = "Program"

        elif current_index == 0:
            table = self.ui.student_table
            table_name = "student"
            code_column_name = "id_number"
            entity_label = "Student"

        else:
            QMessageBox.warning(self, "Error", "Invalid table index.")
            return

        # Get the code value from the row
        item = table.item(row_index, code_column_index)
        if item is None:
            QMessageBox.critical(self, "Error", "Could not get the identifying value from the selected row.")
            return

        code_value = item.text()

        # Confirm deletion
        confirm = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete this {entity_label.lower()}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            try:
                mydb = get_connection()
                mycursor = mydb.cursor()

                sql = f"DELETE FROM {table_name} WHERE {code_column_name} = %s"
                mycursor.execute(sql, (code_value,))
                mydb.commit()

                QMessageBox.information(self, "Deleted", f"{entity_label} deleted successfully.")
                self.load_to_gui()
                self.search(current_index)

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", str(err))

            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()

    def sort_by(self, current_index):
        self.search(current_index)
        table = None
        table_name = None
        sql = ""

        if current_index == 2:
            table = self.ui.college_table
            table_name = "college"
            headers = ["College Code", "College Name", "Actions"]
            index = self.ui.college_sort_by_comboBox.currentIndex()
            if index == 0:
                sql = f"SELECT * FROM {table_name} ORDER BY college_code ASC, college_name ASC"
            elif index == 1:
                sql = f"SELECT * FROM {table_name} ORDER BY college_code DESC, college_name ASC"
            elif index == 2:
                sql = f"SELECT * FROM {table_name} ORDER BY college_name ASC, college_code ASC"
            elif index == 3:
                sql = f"SELECT * FROM {table_name} ORDER BY college_name DESC, college_code ASC"

        elif current_index == 1:
            table = self.ui.program_table
            table_name = "program"
            headers = ["Program Code", "Program Name", "College Code", "Actions"]
            index = self.ui.program_sort_by_comboBox.currentIndex()
            options = [
                "program_code ASC, program_name ASC", 
                "program_code DESC, program_name ASC",
                "program_name ASC, program_code ASC", 
                "program_name DESC, program_code ASC",
                "college_code ASC, program_code ASC", 
                "college_code DESC, program_code ASC"
                ]

            if 0 <= index < len(options):
                sql = f"SELECT * FROM {table_name} ORDER BY {options[index]}"

        elif current_index == 0:
            table = self.ui.student_table
            table_name = "student"
            headers = ["ID Number", "First Name", "Last Name", "Gender", "Year Level", "Program Code", "Actions"]
            index = self.ui.student_sort_by_comboBox.currentIndex()
            options = [
                "id_number ASC, last_name ASC", "id_number DESC, last_name ASC",
                "program_code ASC, last_name ASC", "program_code DESC, last_name ASC",
                "year_level ASC, last_name ASC", "year_level DESC, last_name ASC",
                "first_name ASC, id_number ASC", "first_name DESC, id_number ASC",
                "last_name ASC, id_number ASC", "last_name DESC, id_number ASC",
                "gender ASC, last_name ASC"
                ]
            if 0 <= index < len(options):
                sql = f"SELECT * FROM {table_name} ORDER BY {options[index]}"

        else:
            print("Invalid index")
            return

        try:
            mydb = get_connection()
            mycursor = mydb.cursor()
            mycursor.execute(sql)
            result = mycursor.fetchall()

            table.setRowCount(0)

            for row_num, row_data in enumerate(result):
                table.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

                action_widget = QWidget()
                layout = QHBoxLayout(action_widget)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(5)

                edit_button = QPushButton("Edit")
                edit_button.setStyleSheet("background-color: #FFD700; font-weight: bold;")
                edit_button.clicked.connect(lambda _, r=row_num: self.edit_row(r, current_index))
                layout.addWidget(edit_button)

                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet("background-color: #FF6347; font-weight: bold;")
                delete_button.clicked.connect(lambda _, r=row_num: self.delete_row(r, current_index))
                layout.addWidget(delete_button)

                action_widget.setLayout(layout)
                table.setCellWidget(row_num, len(headers) - 1, action_widget)

        except Exception as e:
            print("Error during sort:", e)

        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()

    def default_search_filter(self, index):
        if index == 2:
            self.ui.college_filter_comboBox.setCurrentIndex(0) #College code
        elif index == 1:
            self.ui.program_filter_comboBox.setCurrentIndex(0) #Program Code
        elif index == 0:
            self.ui.student_filter_comboBox.setCurrentIndex(0) #ID Number

    def search(self, current_index):
        table = None
        search_text = None
        search_filter = None
        table_name = None

        college_filter_map = {
            "college code": "college_code",
            "college name": "college_name",
        }

        program_filter_map = {
            "program code": "program_code",
            "program name": "program_name",
            "college code": "college_code"
        }

        student_filter_map = {
            "id number": "id_number",
            "first name": "first_name",
            "last name": "last_name",
            "gender": "gender",
            "year level": "year_level",
            "program code": "program_code",
        }


        if current_index == 2:
            table = self.ui.college_table
            table_name = "college"
            headers = ["College Code", "College Name", "Actions"]
            search_text = self.ui.college_search_input.text().strip().lower()
            search_filter = self.ui.college_filter_comboBox.currentText().strip().lower()
            filter_map = college_filter_map.get(search_filter, "college_code")

        elif current_index == 1:
            table = self.ui.program_table
            table_name = "program"
            headers = ["Program Code", "Program Name", "College Code", "Actions"]
            search_text = self.ui.program_search_input.text().strip().lower()
            search_filter = self.ui.program_filter_comboBox.currentText().strip().lower()
            filter_map = program_filter_map.get(search_filter, "program_code")

        elif current_index == 0:
            table = self.ui.student_table
            table_name = "student"
            headers = ["ID Number", "First Name", "Last Name", "Gender", "Year Level", "Program Code", "Actions"]
            search_text = self.ui.student_search_input.text().strip().lower()
            search_filter = self.ui.student_filter_comboBox.currentText().strip().lower()
            filter_map = student_filter_map.get(search_filter, "id_number")

        else:
            print("Error at search and search filter")
            return
        
        try:
            mydb = get_connection()
            mycursor = mydb.cursor()

            sql = f"SELECT * FROM {table_name} WHERE LOWER(`{filter_map}`) LIKE %s"
            mycursor.execute(sql, (f"%{search_text}%",))
            result = mycursor.fetchall()

            table.setRowCount(0)

            for row_num, row_data in enumerate(result):
                table.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    table.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

                action_widget = QWidget()
                layout = QHBoxLayout(action_widget)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(5)

                edit_button = QPushButton("Edit")
                edit_button.setStyleSheet("background-color: #FFD700; font-weight: bold;")
                edit_button.clicked.connect(lambda _, r=row_num: self.edit_row(r, current_index))
                layout.addWidget(edit_button)

                delete_button = QPushButton("Delete")
                delete_button.setStyleSheet("background-color: #FF6347; font-weight: bold;")
                delete_button.clicked.connect(lambda _, r=row_num: self.delete_row(r, current_index))
                layout.addWidget(delete_button)

                action_widget.setLayout(layout)
                table.setCellWidget(row_num, len(headers) - 1, action_widget)

        except Exception as e:
            print("Error during search:", e)

        finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    with open("styles/main_gui.qss", "r") as file:
        qss = file.read()
        window.setStyleSheet(qss)

    window.show()
    sys.exit(app.exec())
