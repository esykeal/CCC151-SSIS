from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from db_connection import get_connection

def load_college_data(table_widget):
    try:
        mydb = get_connection()
        mycursor = mydb.cursor()
        results = mycursor.fetchall()

        table_widget.setRowCount(len(results))

    except:
        print("temp")