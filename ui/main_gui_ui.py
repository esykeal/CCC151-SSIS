# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
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
        MainWindow.resize(1092, 700)
        MainWindow.setMinimumSize(QSize(816, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_24 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_17 = QWidget(self.centralwidget)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(121, 803))
        self.verticalLayout_7 = QVBoxLayout(self.widget_17)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sb_ssis_label_2 = QLabel(self.widget_17)
        self.sb_ssis_label_2.setObjectName(u"sb_ssis_label_2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.sb_ssis_label_2.setFont(font)

        self.verticalLayout_5.addWidget(self.sb_ssis_label_2)

        self.sidebar_show_pushButton = QPushButton(self.widget_17)
        self.sidebar_show_pushButton.setObjectName(u"sidebar_show_pushButton")
        self.sidebar_show_pushButton.setMinimumSize(QSize(61, 51))
        self.sidebar_show_pushButton.setMaximumSize(QSize(61, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.sidebar_show_pushButton.setFont(font1)
        self.sidebar_show_pushButton.setCheckable(True)

        self.verticalLayout_5.addWidget(self.sidebar_show_pushButton)

        self.student_pushButton = QPushButton(self.widget_17)
        self.student_pushButton.setObjectName(u"student_pushButton")
        self.student_pushButton.setMinimumSize(QSize(61, 51))
        self.student_pushButton.setMaximumSize(QSize(61, 51))
        self.student_pushButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.student_pushButton)

        self.program_pushButton = QPushButton(self.widget_17)
        self.program_pushButton.setObjectName(u"program_pushButton")
        self.program_pushButton.setMinimumSize(QSize(61, 51))
        self.program_pushButton.setMaximumSize(QSize(61, 51))
        self.program_pushButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.program_pushButton)

        self.college_pushButton = QPushButton(self.widget_17)
        self.college_pushButton.setObjectName(u"college_pushButton")
        self.college_pushButton.setMinimumSize(QSize(61, 51))
        self.college_pushButton.setMaximumSize(QSize(61, 51))
        self.college_pushButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.college_pushButton)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 465, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.exit_pushButton = QPushButton(self.widget_17)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setMinimumSize(QSize(61, 51))
        self.exit_pushButton.setMaximumSize(QSize(61, 51))
        self.exit_pushButton.setFont(font1)

        self.verticalLayout_6.addWidget(self.exit_pushButton)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_24.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.centralwidget)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_2 = QVBoxLayout(self.widget_18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)

        self.sb_ssis_label = QLabel(self.widget_18)
        self.sb_ssis_label.setObjectName(u"sb_ssis_label")
        self.sb_ssis_label.setFont(font)

        self.horizontalLayout_17.addWidget(self.sb_ssis_label)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.sidebar_hide_pushButton = QPushButton(self.widget_18)
        self.sidebar_hide_pushButton.setObjectName(u"sidebar_hide_pushButton")
        self.sidebar_hide_pushButton.setMinimumSize(QSize(61, 51))
        self.sidebar_hide_pushButton.setMaximumSize(QSize(61, 51))
        self.sidebar_hide_pushButton.setFont(font1)
        self.sidebar_hide_pushButton.setCheckable(True)

        self.horizontalLayout_23.addWidget(self.sidebar_hide_pushButton)

        self.label = QLabel(self.widget_18)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout_23.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.student_pushButton_2 = QPushButton(self.widget_18)
        self.student_pushButton_2.setObjectName(u"student_pushButton_2")
        self.student_pushButton_2.setMinimumSize(QSize(61, 51))
        self.student_pushButton_2.setMaximumSize(QSize(61, 51))
        self.student_pushButton_2.setFont(font1)

        self.horizontalLayout_22.addWidget(self.student_pushButton_2)

        self.sb_student_label = QLabel(self.widget_18)
        self.sb_student_label.setObjectName(u"sb_student_label")
        self.sb_student_label.setFont(font2)

        self.horizontalLayout_22.addWidget(self.sb_student_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.program_pushButton_2 = QPushButton(self.widget_18)
        self.program_pushButton_2.setObjectName(u"program_pushButton_2")
        self.program_pushButton_2.setMinimumSize(QSize(61, 51))
        self.program_pushButton_2.setMaximumSize(QSize(61, 51))
        self.program_pushButton_2.setFont(font1)

        self.horizontalLayout_21.addWidget(self.program_pushButton_2)

        self.sb_program_label = QLabel(self.widget_18)
        self.sb_program_label.setObjectName(u"sb_program_label")
        self.sb_program_label.setFont(font2)

        self.horizontalLayout_21.addWidget(self.sb_program_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.college_pushButton_2 = QPushButton(self.widget_18)
        self.college_pushButton_2.setObjectName(u"college_pushButton_2")
        self.college_pushButton_2.setMinimumSize(QSize(61, 51))
        self.college_pushButton_2.setMaximumSize(QSize(61, 51))
        self.college_pushButton_2.setFont(font1)

        self.horizontalLayout_20.addWidget(self.college_pushButton_2)

        self.sb_college_label = QLabel(self.widget_18)
        self.sb_college_label.setObjectName(u"sb_college_label")
        self.sb_college_label.setFont(font2)

        self.horizontalLayout_20.addWidget(self.sb_college_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_2 = QSpacerItem(20, 449, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_22 = QWidget(self.widget_18)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(158, 69))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.exit_pushButton_2 = QPushButton(self.widget_22)
        self.exit_pushButton_2.setObjectName(u"exit_pushButton_2")
        self.exit_pushButton_2.setMinimumSize(QSize(61, 51))
        self.exit_pushButton_2.setFont(font1)

        self.horizontalLayout_19.addWidget(self.exit_pushButton_2)

        self.exit_label = QLabel(self.widget_22)
        self.exit_label.setObjectName(u"exit_label")
        self.exit_label.setFont(font2)

        self.horizontalLayout_19.addWidget(self.exit_label)


        self.verticalLayout_2.addWidget(self.widget_22)


        self.horizontalLayout_24.addWidget(self.widget_18)

        self.widget_16 = QWidget(self.centralwidget)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.stackedWidget = QStackedWidget(self.widget_16)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.student_label = QLabel(self.widget_2)
        self.student_label.setObjectName(u"student_label")
        self.student_label.setMinimumSize(QSize(211, 41))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.student_label.setFont(font3)
        self.student_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.student_label)

        self.horizontalSpacer_4 = QSpacerItem(428, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.student_search_input = QLineEdit(self.widget_3)
        self.student_search_input.setObjectName(u"student_search_input")
        self.student_search_input.setMinimumSize(QSize(311, 27))
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
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.student_filter_label.setFont(font4)

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


        self.verticalLayout.addWidget(self.widget)

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
        self.add_student_button.setFont(font4)
        self.add_student_button.setLayoutDirection(Qt.LeftToRight)
        self.add_student_button.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.add_student_button)


        self.verticalLayout.addWidget(self.widget_5)

        self.student_table = QTableWidget(self.page)
        if (self.student_table.columnCount() < 7):
            self.student_table.setColumnCount(7)
        self.student_table.setObjectName(u"student_table")
        self.student_table.setColumnCount(7)
        self.student_table.horizontalHeader().setProperty(u"showSortIndicator", False)

        self.verticalLayout.addWidget(self.student_table)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_14 = QWidget(self.page_2)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.program_label = QLabel(self.widget_14)
        self.program_label.setObjectName(u"program_label")
        self.program_label.setMinimumSize(QSize(211, 41))
        self.program_label.setFont(font3)
        self.program_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.program_label)

        self.horizontalSpacer_10 = QSpacerItem(541, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addWidget(self.widget_14)

        self.widget_6 = QWidget(self.page_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
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
        self.program_filter_label.setFont(font4)

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


        self.verticalLayout_3.addWidget(self.widget_6)

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

        self.horizontalSpacer_9 = QSpacerItem(329, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.add_program_button = QPushButton(self.widget_12)
        self.add_program_button.setObjectName(u"add_program_button")
        self.add_program_button.setMinimumSize(QSize(161, 41))
        self.add_program_button.setFont(font4)
        self.add_program_button.setLayoutDirection(Qt.LeftToRight)
        self.add_program_button.setAutoFillBackground(False)

        self.horizontalLayout_11.addWidget(self.add_program_button)


        self.verticalLayout_3.addWidget(self.widget_12)

        self.program_table = QTableWidget(self.page_2)
        if (self.program_table.columnCount() < 4):
            self.program_table.setColumnCount(4)
        self.program_table.setObjectName(u"program_table")
        self.program_table.setColumnCount(4)

        self.verticalLayout_3.addWidget(self.program_table)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_13 = QWidget(self.page_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.college_label = QLabel(self.widget_13)
        self.college_label.setObjectName(u"college_label")
        self.college_label.setMinimumSize(QSize(211, 41))
        self.college_label.setFont(font3)
        self.college_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.college_label)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)


        self.verticalLayout_4.addWidget(self.widget_13)

        self.widget_9 = QWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
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
        self.college_filter_label.setFont(font4)

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


        self.verticalLayout_4.addWidget(self.widget_9)

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
        self.add_college_button.setFont(font4)
        self.add_college_button.setLayoutDirection(Qt.LeftToRight)
        self.add_college_button.setAutoFillBackground(False)

        self.horizontalLayout_13.addWidget(self.add_college_button)


        self.verticalLayout_4.addWidget(self.widget_15)

        self.college_table = QTableWidget(self.page_3)
        if (self.college_table.columnCount() < 3):
            self.college_table.setColumnCount(3)
        self.college_table.setObjectName(u"college_table")
        self.college_table.setColumnCount(3)

        self.verticalLayout_4.addWidget(self.college_table)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_16.addWidget(self.stackedWidget)


        self.horizontalLayout_24.addWidget(self.widget_16)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.sidebar_show_pushButton.pressed.connect(self.widget_17.hide)
        self.sidebar_hide_pushButton.pressed.connect(self.widget_18.hide)
        self.sidebar_hide_pushButton.pressed.connect(self.widget_17.show)
        self.sidebar_show_pushButton.pressed.connect(self.widget_18.show)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sb_ssis_label_2.setText(QCoreApplication.translate("MainWindow", u"SSIS v2", None))
        self.sidebar_show_pushButton.setText("")
        self.student_pushButton.setText("")
        self.program_pushButton.setText("")
        self.college_pushButton.setText("")
        self.exit_pushButton.setText("")
        self.sb_ssis_label.setText(QCoreApplication.translate("MainWindow", u"SSIS v2", None))
        self.sidebar_hide_pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.student_pushButton_2.setText("")
        self.sb_student_label.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.program_pushButton_2.setText("")
        self.sb_program_label.setText(QCoreApplication.translate("MainWindow", u"Programs", None))
        self.college_pushButton_2.setText("")
        self.sb_college_label.setText(QCoreApplication.translate("MainWindow", u"Colleges", None))
        self.exit_pushButton_2.setText("")
        self.exit_label.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.student_label.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.student_search_input.setText("")
        self.student_search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
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
        self.program_search_input.setText("")
        self.program_search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
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
        self.college_search_input.setText("")
        self.college_search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
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

