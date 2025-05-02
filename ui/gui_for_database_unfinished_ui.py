# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_for_database_unfinished.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 831)
        MainWindow.setMinimumSize(QSize(816, 831))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.student_label = QLabel(self.widget_2)
        self.student_label.setObjectName(u"student_label")
        self.student_label.setMinimumSize(QSize(211, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.student_label.setFont(font)
        self.student_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.student_label)

        self.horizontalSpacer_4 = QSpacerItem(743, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.student_search_input = QLineEdit(self.widget_3)
        self.student_search_input.setObjectName(u"student_search_input")
        self.student_search_input.setMinimumSize(QSize(311, 27))
        font1 = QFont()
        font1.setPointSize(12)
        self.student_search_input.setFont(font1)

        self.horizontalLayout_2.addWidget(self.student_search_input)

        self.student_search_button = QPushButton(self.widget_3)
        self.student_search_button.setObjectName(u"student_search_button")
        self.student_search_button.setMinimumSize(QSize(49, 30))
        self.student_search_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.student_search_button)


        self.horizontalLayout_14.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.student_filter_label = QLabel(self.widget_4)
        self.student_filter_label.setObjectName(u"student_filter_label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.student_filter_label.setFont(font2)

        self.horizontalLayout_6.addWidget(self.student_filter_label)

        self.student_filter_comboBox = QComboBox(self.widget_4)
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.addItem("")
        self.student_filter_comboBox.setObjectName(u"student_filter_comboBox")
        self.student_filter_comboBox.setMinimumSize(QSize(156, 30))
        self.student_filter_comboBox.setFont(font1)

        self.horizontalLayout_6.addWidget(self.student_filter_comboBox)


        self.horizontalLayout_14.addWidget(self.widget_4)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(291, 61))
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.student_sort_by_label = QLabel(self.widget_5)
        self.student_sort_by_label.setObjectName(u"student_sort_by_label")
        self.student_sort_by_label.setMinimumSize(QSize(61, 41))
        self.student_sort_by_label.setFont(font1)

        self.horizontalLayout.addWidget(self.student_sort_by_label)

        self.student_sort_by_comboBox = QComboBox(self.widget_5)
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.addItem("")
        self.student_sort_by_comboBox.setObjectName(u"student_sort_by_comboBox")
        self.student_sort_by_comboBox.setMinimumSize(QSize(200, 30))
        self.student_sort_by_comboBox.setFont(font1)

        self.horizontalLayout.addWidget(self.student_sort_by_comboBox)

        self.horizontalSpacer_3 = QSpacerItem(317, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.add_student_button = QPushButton(self.widget_5)
        self.add_student_button.setObjectName(u"add_student_button")
        self.add_student_button.setMinimumSize(QSize(161, 41))
        self.add_student_button.setFont(font2)
        self.add_student_button.setLayoutDirection(Qt.LeftToRight)
        self.add_student_button.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.add_student_button)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.student_table = QTableWidget(self.page)
        if (self.student_table.columnCount() < 7):
            self.student_table.setColumnCount(7)
        self.student_table.setObjectName(u"student_table")
        self.student_table.setColumnCount(7)
        self.student_table.horizontalHeader().setProperty(u"showSortIndicator", False)

        self.verticalLayout_4.addWidget(self.student_table)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_14 = QWidget(self.page_2)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.program_label = QLabel(self.widget_14)
        self.program_label.setObjectName(u"program_label")
        self.program_label.setMinimumSize(QSize(211, 41))
        self.program_label.setFont(font)
        self.program_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.program_label)

        self.horizontalSpacer_10 = QSpacerItem(737, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.widget_14)

        self.widget_6 = QWidget(self.page_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.program_search_input = QLineEdit(self.widget_7)
        self.program_search_input.setObjectName(u"program_search_input")
        self.program_search_input.setMinimumSize(QSize(311, 27))
        self.program_search_input.setFont(font1)

        self.horizontalLayout_4.addWidget(self.program_search_input)

        self.program_search_button = QPushButton(self.widget_7)
        self.program_search_button.setObjectName(u"program_search_button")
        self.program_search_button.setMinimumSize(QSize(49, 30))
        self.program_search_button.setFont(font1)

        self.horizontalLayout_4.addWidget(self.program_search_button)


        self.horizontalLayout_15.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.program_filter_label = QLabel(self.widget_8)
        self.program_filter_label.setObjectName(u"program_filter_label")
        self.program_filter_label.setFont(font2)

        self.horizontalLayout_8.addWidget(self.program_filter_label)

        self.program_filter_comboBox = QComboBox(self.widget_8)
        self.program_filter_comboBox.addItem("")
        self.program_filter_comboBox.addItem("")
        self.program_filter_comboBox.addItem("")
        self.program_filter_comboBox.setObjectName(u"program_filter_comboBox")
        self.program_filter_comboBox.setMinimumSize(QSize(160, 30))
        self.program_filter_comboBox.setFont(font1)

        self.horizontalLayout_8.addWidget(self.program_filter_comboBox)


        self.horizontalLayout_15.addWidget(self.widget_8)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_12 = QWidget(self.page_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.program_sort_label = QLabel(self.widget_12)
        self.program_sort_label.setObjectName(u"program_sort_label")
        self.program_sort_label.setMinimumSize(QSize(61, 41))
        self.program_sort_label.setFont(font1)

        self.horizontalLayout_11.addWidget(self.program_sort_label)

        self.program_sort_by_comboBox = QComboBox(self.widget_12)
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.addItem("")
        self.program_sort_by_comboBox.setObjectName(u"program_sort_by_comboBox")
        self.program_sort_by_comboBox.setMinimumSize(QSize(200, 30))
        self.program_sort_by_comboBox.setFont(font1)

        self.horizontalLayout_11.addWidget(self.program_sort_by_comboBox)

        self.horizontalSpacer_9 = QSpacerItem(525, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.add_program_button = QPushButton(self.widget_12)
        self.add_program_button.setObjectName(u"add_program_button")
        self.add_program_button.setMinimumSize(QSize(161, 41))
        self.add_program_button.setFont(font2)
        self.add_program_button.setLayoutDirection(Qt.LeftToRight)
        self.add_program_button.setAutoFillBackground(False)

        self.horizontalLayout_11.addWidget(self.add_program_button)


        self.verticalLayout_2.addWidget(self.widget_12)

        self.program_table = QTableWidget(self.page_2)
        if (self.program_table.columnCount() < 4):
            self.program_table.setColumnCount(4)
        self.program_table.setObjectName(u"program_table")
        self.program_table.setColumnCount(4)

        self.verticalLayout_2.addWidget(self.program_table)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_13 = QWidget(self.page_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.college_label = QLabel(self.widget_13)
        self.college_label.setObjectName(u"college_label")
        self.college_label.setMinimumSize(QSize(211, 41))
        self.college_label.setFont(font)
        self.college_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.college_label)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)


        self.verticalLayout_3.addWidget(self.widget_13)

        self.widget_9 = QWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.college_search_input = QLineEdit(self.widget_10)
        self.college_search_input.setObjectName(u"college_search_input")
        self.college_search_input.setMinimumSize(QSize(311, 27))
        self.college_search_input.setFont(font1)

        self.horizontalLayout_7.addWidget(self.college_search_input)

        self.college_search_button = QPushButton(self.widget_10)
        self.college_search_button.setObjectName(u"college_search_button")
        self.college_search_button.setMinimumSize(QSize(49, 30))
        self.college_search_button.setFont(font1)

        self.horizontalLayout_7.addWidget(self.college_search_button)


        self.horizontalLayout_12.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.college_filter_label = QLabel(self.widget_11)
        self.college_filter_label.setObjectName(u"college_filter_label")
        self.college_filter_label.setFont(font2)

        self.horizontalLayout_9.addWidget(self.college_filter_label)

        self.college_filter_comboBox = QComboBox(self.widget_11)
        self.college_filter_comboBox.addItem("")
        self.college_filter_comboBox.addItem("")
        self.college_filter_comboBox.setObjectName(u"college_filter_comboBox")
        self.college_filter_comboBox.setMinimumSize(QSize(141, 27))
        self.college_filter_comboBox.setFont(font1)

        self.horizontalLayout_9.addWidget(self.college_filter_comboBox)


        self.horizontalLayout_12.addWidget(self.widget_11)

        self.horizontalSpacer_8 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.widget_15 = QWidget(self.page_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.college_sort_by_label = QLabel(self.widget_15)
        self.college_sort_by_label.setObjectName(u"college_sort_by_label")
        self.college_sort_by_label.setMinimumSize(QSize(61, 41))
        self.college_sort_by_label.setFont(font1)

        self.horizontalLayout_13.addWidget(self.college_sort_by_label)

        self.college_sort_by_comboBox = QComboBox(self.widget_15)
        self.college_sort_by_comboBox.addItem("")
        self.college_sort_by_comboBox.addItem("")
        self.college_sort_by_comboBox.addItem("")
        self.college_sort_by_comboBox.addItem("")
        self.college_sort_by_comboBox.setObjectName(u"college_sort_by_comboBox")
        self.college_sort_by_comboBox.setMinimumSize(QSize(200, 30))
        self.college_sort_by_comboBox.setFont(font1)

        self.horizontalLayout_13.addWidget(self.college_sort_by_comboBox)

        self.horizontalSpacer_12 = QSpacerItem(275, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.add_college_button = QPushButton(self.widget_15)
        self.add_college_button.setObjectName(u"add_college_button")
        self.add_college_button.setMinimumSize(QSize(161, 41))
        self.add_college_button.setFont(font2)
        self.add_college_button.setLayoutDirection(Qt.LeftToRight)
        self.add_college_button.setAutoFillBackground(False)

        self.horizontalLayout_13.addWidget(self.add_college_button)


        self.verticalLayout_3.addWidget(self.widget_15)

        self.college_table = QTableWidget(self.page_3)
        if (self.college_table.columnCount() < 3):
            self.college_table.setColumnCount(3)
        self.college_table.setObjectName(u"college_table")
        self.college_table.setColumnCount(3)

        self.verticalLayout_3.addWidget(self.college_table)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.student_label.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_search_input.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.student_search_button.setText("")
        self.student_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filters:", None))
        self.student_filter_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.student_filter_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Program Code", None))
        self.student_filter_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"First Name", None))
        self.student_filter_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.student_filter_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.student_filter_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Year Level", None))

        self.student_sort_by_label.setText(QCoreApplication.translate("MainWindow", u"Sort By:", None))
        self.student_sort_by_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ID Num (asc)", None))
        self.student_sort_by_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ID Num (desc)", None))
        self.student_sort_by_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Program Code (asc)", None))
        self.student_sort_by_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Program Code (desc)", None))
        self.student_sort_by_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Year Level (asc)", None))
        self.student_sort_by_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Year Level (desc)", None))
        self.student_sort_by_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"First Name (A-Z)", None))
        self.student_sort_by_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"First Name (Z-A)", None))
        self.student_sort_by_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Last Name (A-Z)", None))
        self.student_sort_by_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Gender", None))

        self.add_student_button.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.program_label.setText(QCoreApplication.translate("MainWindow", u"Program Information", None))
        self.program_search_input.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.program_search_button.setText("")
        self.program_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filters:", None))
        self.program_filter_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Program Code", None))
        self.program_filter_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Program Name", None))
        self.program_filter_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"College Code", None))

        self.program_sort_label.setText(QCoreApplication.translate("MainWindow", u"Sort By:", None))
        self.program_sort_by_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Program Code (A-Z)", None))
        self.program_sort_by_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Program Code (Z-A)", None))
        self.program_sort_by_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Program Name (A-Z)", None))
        self.program_sort_by_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Program Name (Z-A)", None))
        self.program_sort_by_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"College Code (A-Z)", None))
        self.program_sort_by_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"College Code (Z-A)", None))

        self.add_program_button.setText(QCoreApplication.translate("MainWindow", u"Add Program", None))
        self.college_label.setText(QCoreApplication.translate("MainWindow", u"College Information", None))
        self.college_search_input.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.college_search_button.setText("")
        self.college_filter_label.setText(QCoreApplication.translate("MainWindow", u"Filters:", None))
        self.college_filter_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"College Code", None))
        self.college_filter_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"College Name", None))

        self.college_sort_by_label.setText(QCoreApplication.translate("MainWindow", u"Sort By:", None))
        self.college_sort_by_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"College Code (A-Z)", None))
        self.college_sort_by_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"College Code (Z-A)", None))
        self.college_sort_by_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"College Name (A-Z)", None))
        self.college_sort_by_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"College Name (Z-A)", None))

        self.add_college_button.setText(QCoreApplication.translate("MainWindow", u"Add College", None))
    # retranslateUi

