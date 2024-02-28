# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(640, 490))
        MainWindow.setMaximumSize(QtCore.QSize(640, 490))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("/* QPushButton Style */\n"
"QPushButton {\n"
"    background-color: #4CAF50; \n"
"    color: white; \n"
"    border: 2px solid #45a049; \n"
"    border-radius: 5px; \n"
"    padding: 8px 16px;\n"
"    font-size: 14px; \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3e8e41; \n"
"}\n"
"QLCDNumber {\n"
" color: black;\n"
"}")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 2, 0, 1, 1)
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setObjectName("calculate_btn")
        self.gridLayout_7.addWidget(self.calculate_btn, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 5, 0, 1, 4)
        self.mainmenu_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mainmenu_btn.setObjectName("mainmenu_btn")
        self.gridLayout_7.addWidget(self.mainmenu_btn, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 2, 3, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setStyleSheet("            QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 2px solid rgba(0, 0, 0, 120);\n"
"                border-radius: 8px;\n"
"                margin-top: 10px;\n"
"                background-color: #ecf0f1;\n"
"            }\n"
"            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top center;\n"
"                padding: 0 3px;\n"
"                background-color:rgba(0, 0, 0, 190);\n"
"                color: white;\n"
"            }")
        self.MainPage.setObjectName("MainPage")
        self.gridLayout = QtWidgets.QGridLayout(self.MainPage)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.MainPage)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 3)
        self.Select_btn = QtWidgets.QPushButton(self.MainPage)
        self.Select_btn.setObjectName("Select_btn")
        self.gridLayout.addWidget(self.Select_btn, 5, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 1, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 6, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.MainPage)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 130))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 150))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.circle_radioButton = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.circle_radioButton.setFont(font)
        self.circle_radioButton.setChecked(True)
        self.circle_radioButton.setObjectName("circle_radioButton")
        self.FiguresButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.FiguresButtonGroup.setObjectName("FiguresButtonGroup")
        self.FiguresButtonGroup.addButton(self.circle_radioButton)
        self.verticalLayout.addWidget(self.circle_radioButton)
        self.triangle_radioButton = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.triangle_radioButton.setFont(font)
        self.triangle_radioButton.setObjectName("triangle_radioButton")
        self.FiguresButtonGroup.addButton(self.triangle_radioButton)
        self.verticalLayout.addWidget(self.triangle_radioButton)
        self.rectangle_radioButton = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rectangle_radioButton.setFont(font)
        self.rectangle_radioButton.setObjectName("rectangle_radioButton")
        self.FiguresButtonGroup.addButton(self.rectangle_radioButton)
        self.verticalLayout.addWidget(self.rectangle_radioButton)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.FiguresButtonGroup.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.MainPage)
        self.groupBox_2.setMinimumSize(QtCore.QSize(140, 130))
        self.groupBox_2.setMaximumSize(QtCore.QSize(140, 150))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.ColorButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.ColorButtonGroup.setObjectName("ColorButtonGroup")
        self.ColorButtonGroup.addButton(self.radioButton_5)
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.ColorButtonGroup.addButton(self.radioButton_8)
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.ColorButtonGroup.addButton(self.radioButton_6)
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.ColorButtonGroup.addButton(self.radioButton_7)
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.gridLayout.addWidget(self.groupBox_2, 3, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 3, 2, 1, 1)
        self.stackedWidget.addWidget(self.MainPage)
        self.CirclePage = QtWidgets.QWidget()
        self.CirclePage.setObjectName("CirclePage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.CirclePage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.CirclePage)
        self.groupBox_3.setMinimumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.groupBox_3.setTitle("Circle")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setContentsMargins(9, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 3, 0, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 3, 8, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 1, 2, 1, 6)
        self.radius_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.radius_spinbox.setMinimumSize(QtCore.QSize(90, 25))
        self.radius_spinbox.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radius_spinbox.setFont(font)
        self.radius_spinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.radius_spinbox.setObjectName("radius_spinbox")
        self.gridLayout_4.addWidget(self.radius_spinbox, 2, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 3, 6, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem14, 5, 7, 1, 1)
        self.Circle_lbl = QtWidgets.QLabel(self.groupBox_3)
        self.Circle_lbl.setMinimumSize(QtCore.QSize(300, 300))
        self.Circle_lbl.setMaximumSize(QtCore.QSize(600, 600))
        self.Circle_lbl.setSizeIncrement(QtCore.QSize(50, 10))
        self.Circle_lbl.setObjectName("Circle_lbl")
        self.gridLayout_4.addWidget(self.Circle_lbl, 2, 7, 3, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        self.frame.setMinimumSize(QtCore.QSize(190, 50))
        self.frame.setMaximumSize(QtCore.QSize(240, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.circle_area_lbl = QtWidgets.QLabel(self.frame)
        self.circle_area_lbl.setMinimumSize(QtCore.QSize(70, 25))
        self.circle_area_lbl.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.circle_area_lbl.setFont(font)
        self.circle_area_lbl.setObjectName("circle_area_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.circle_area_lbl)
        self.circle_area_lcd = QtWidgets.QLCDNumber(self.frame)
        self.circle_area_lcd.setMinimumSize(QtCore.QSize(120, 25))
        self.circle_area_lcd.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.circle_area_lcd.setFont(font)
        self.circle_area_lcd.setObjectName("circle_area_lcd")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.circle_area_lcd)
        self.circle_length_lbl = QtWidgets.QLabel(self.frame)
        self.circle_length_lbl.setMinimumSize(QtCore.QSize(70, 25))
        self.circle_length_lbl.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.circle_length_lbl.setFont(font)
        self.circle_length_lbl.setObjectName("circle_length_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.circle_length_lbl)
        self.circle_length_lcd = QtWidgets.QLCDNumber(self.frame)
        self.circle_length_lcd.setMinimumSize(QtCore.QSize(120, 25))
        self.circle_length_lcd.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.circle_length_lcd.setFont(font)
        self.circle_length_lcd.setObjectName("circle_length_lcd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.circle_length_lcd)
        self.gridLayout_4.addWidget(self.frame, 4, 3, 1, 3)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setMinimumSize(QtCore.QSize(100, 25))
        self.label.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.CirclePage)
        self.TrianglePage = QtWidgets.QWidget()
        self.TrianglePage.setObjectName("TrianglePage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TrianglePage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.TrianglePage)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem15, 8, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_2.setMinimumSize(QtCore.QSize(190, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(240, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.triangle_area_lbl = QtWidgets.QLabel(self.frame_2)
        self.triangle_area_lbl.setMinimumSize(QtCore.QSize(100, 25))
        self.triangle_area_lbl.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.triangle_area_lbl.setFont(font)
        self.triangle_area_lbl.setObjectName("triangle_area_lbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.triangle_area_lbl)
        self.triangle_area_lcd = QtWidgets.QLCDNumber(self.frame_2)
        self.triangle_area_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.triangle_area_lcd.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.triangle_area_lcd.setFont(font)
        self.triangle_area_lcd.setObjectName("triangle_area_lcd")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.triangle_area_lcd)
        self.triangle_perimeter_lbl = QtWidgets.QLabel(self.frame_2)
        self.triangle_perimeter_lbl.setMinimumSize(QtCore.QSize(100, 25))
        self.triangle_perimeter_lbl.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.triangle_perimeter_lbl.setFont(font)
        self.triangle_perimeter_lbl.setObjectName("triangle_perimeter_lbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.triangle_perimeter_lbl)
        self.triangle_perimeter_lcd = QtWidgets.QLCDNumber(self.frame_2)
        self.triangle_perimeter_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.triangle_perimeter_lcd.setMaximumSize(QtCore.QSize(120, 30))
        self.triangle_perimeter_lcd.setObjectName("triangle_perimeter_lcd")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.triangle_perimeter_lcd)
        self.gridLayout_8.addWidget(self.frame_2, 7, 1, 1, 2)
        self.triangle_ds = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds.setMinimumSize(QtCore.QSize(90, 25))
        self.triangle_ds.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.triangle_ds.setFont(font)
        self.triangle_ds.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.triangle_ds.setObjectName("triangle_ds")
        self.gridLayout_8.addWidget(self.triangle_ds, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setMinimumSize(QtCore.QSize(100, 25))
        self.label_5.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setMinimumSize(QtCore.QSize(100, 25))
        self.label_6.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setMinimumSize(QtCore.QSize(100, 25))
        self.label_7.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 4, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem16, 6, 5, 1, 1)
        self.triangle_ds_3 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds_3.setMinimumSize(QtCore.QSize(90, 25))
        self.triangle_ds_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.triangle_ds_3.setFont(font)
        self.triangle_ds_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.triangle_ds_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.triangle_ds_3.setObjectName("triangle_ds_3")
        self.gridLayout_8.addWidget(self.triangle_ds_3, 1, 2, 1, 1)
        self.triangle_ds_2 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds_2.setMinimumSize(QtCore.QSize(90, 25))
        self.triangle_ds_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.triangle_ds_2.setFont(font)
        self.triangle_ds_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.triangle_ds_2.setObjectName("triangle_ds_2")
        self.gridLayout_8.addWidget(self.triangle_ds_2, 2, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem17, 6, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem18, 6, 0, 1, 1)
        self.triangle_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.triangle_lbl.setMinimumSize(QtCore.QSize(300, 300))
        self.triangle_lbl.setMaximumSize(QtCore.QSize(900, 900))
        self.triangle_lbl.setSizeIncrement(QtCore.QSize(50, 10))
        self.triangle_lbl.setObjectName("triangle_lbl")
        self.gridLayout_8.addWidget(self.triangle_lbl, 1, 4, 7, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem19, 0, 1, 1, 4)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.TrianglePage)
        self.RectanglePage = QtWidgets.QWidget()
        self.RectanglePage.setObjectName("RectanglePage")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.RectanglePage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.RectanglePage)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_5)
        self.frame_3.setMinimumSize(QtCore.QSize(190, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(240, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.rectangle_area_lbl = QtWidgets.QLabel(self.frame_3)
        self.rectangle_area_lbl.setMinimumSize(QtCore.QSize(100, 25))
        self.rectangle_area_lbl.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rectangle_area_lbl.setFont(font)
        self.rectangle_area_lbl.setObjectName("rectangle_area_lbl")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rectangle_area_lbl)
        self.rectangle_perimeter_lbl = QtWidgets.QLabel(self.frame_3)
        self.rectangle_perimeter_lbl.setMinimumSize(QtCore.QSize(100, 25))
        self.rectangle_perimeter_lbl.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rectangle_perimeter_lbl.setFont(font)
        self.rectangle_perimeter_lbl.setObjectName("rectangle_perimeter_lbl")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rectangle_perimeter_lbl)
        self.rectangle_area_lcd = QtWidgets.QLCDNumber(self.frame_3)
        self.rectangle_area_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.rectangle_area_lcd.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectangle_area_lcd.setFont(font)
        self.rectangle_area_lcd.setObjectName("rectangle_area_lcd")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rectangle_area_lcd)
        self.rectangle_perimeter_lcd = QtWidgets.QLCDNumber(self.frame_3)
        self.rectangle_perimeter_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.rectangle_perimeter_lcd.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rectangle_perimeter_lcd.setFont(font)
        self.rectangle_perimeter_lcd.setObjectName("rectangle_perimeter_lcd")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rectangle_perimeter_lcd)
        self.gridLayout_9.addWidget(self.frame_3, 5, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setMinimumSize(QtCore.QSize(100, 25))
        self.label_8.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 3, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem20, 6, 4, 1, 1)
        self.rectangle_ds = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.rectangle_ds.setMinimumSize(QtCore.QSize(90, 25))
        self.rectangle_ds.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rectangle_ds.setFont(font)
        self.rectangle_ds.setObjectName("rectangle_ds")
        self.gridLayout_9.addWidget(self.rectangle_ds, 1, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem21, 4, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 1, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem22, 4, 3, 1, 1)
        self.rectangle_ds_2 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.rectangle_ds_2.setMinimumSize(QtCore.QSize(90, 25))
        self.rectangle_ds_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rectangle_ds_2.setFont(font)
        self.rectangle_ds_2.setObjectName("rectangle_ds_2")
        self.gridLayout_9.addWidget(self.rectangle_ds_2, 3, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem23, 4, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(525, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem24, 0, 1, 1, 4)
        self.Rectangle_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.Rectangle_lbl.setMinimumSize(QtCore.QSize(300, 300))
        self.Rectangle_lbl.setMaximumSize(QtCore.QSize(300, 300))
        self.Rectangle_lbl.setObjectName("Rectangle_lbl")
        self.gridLayout_9.addWidget(self.Rectangle_lbl, 1, 4, 5, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.RectanglePage)
        self.ParallelogramPage = QtWidgets.QWidget()
        self.ParallelogramPage.setObjectName("ParallelogramPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ParallelogramPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_6 = QtWidgets.QGroupBox(self.ParallelogramPage)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem25, 4, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem26, 4, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem27, 4, 5, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem28, 6, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_10.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setMinimumSize(QtCore.QSize(100, 25))
        self.label_11.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_10.addWidget(self.label_11, 2, 1, 1, 1)
        self.parallelogram_ds = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.parallelogram_ds.setMinimumSize(QtCore.QSize(90, 25))
        self.parallelogram_ds.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parallelogram_ds.setFont(font)
        self.parallelogram_ds.setObjectName("parallelogram_ds")
        self.gridLayout_10.addWidget(self.parallelogram_ds, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setMinimumSize(QtCore.QSize(100, 25))
        self.label_12.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 3, 1, 1, 1)
        self.parallelogram_ds_2 = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.parallelogram_ds_2.setMinimumSize(QtCore.QSize(90, 25))
        self.parallelogram_ds_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parallelogram_ds_2.setFont(font)
        self.parallelogram_ds_2.setObjectName("parallelogram_ds_2")
        self.gridLayout_10.addWidget(self.parallelogram_ds_2, 2, 2, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem29, 0, 1, 1, 4)
        self.parallelogram_angle_ds = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.parallelogram_angle_ds.setMinimumSize(QtCore.QSize(90, 25))
        self.parallelogram_angle_ds.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.parallelogram_angle_ds.setFont(font)
        self.parallelogram_angle_ds.setMaximum(180.99)
        self.parallelogram_angle_ds.setObjectName("parallelogram_angle_ds")
        self.gridLayout_10.addWidget(self.parallelogram_angle_ds, 3, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.groupBox_6)
        self.frame_4.setMinimumSize(QtCore.QSize(190, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(240, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.parallelogram_area_lbl = QtWidgets.QLabel(self.frame_4)
        self.parallelogram_area_lbl.setMinimumSize(QtCore.QSize(100, 25))
        self.parallelogram_area_lbl.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.parallelogram_area_lbl.setFont(font)
        self.parallelogram_area_lbl.setObjectName("parallelogram_area_lbl")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.parallelogram_area_lbl)
        self.parallelogram_area_lcd = QtWidgets.QLCDNumber(self.frame_4)
        self.parallelogram_area_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.parallelogram_area_lcd.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parallelogram_area_lcd.setFont(font)
        self.parallelogram_area_lcd.setObjectName("parallelogram_area_lcd")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.parallelogram_area_lcd)
        self.parallelogram_perimeter_lbl = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.parallelogram_perimeter_lbl.setFont(font)
        self.parallelogram_perimeter_lbl.setObjectName("parallelogram_perimeter_lbl")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.parallelogram_perimeter_lbl)
        self.parallelogram_perimeter_lcd = QtWidgets.QLCDNumber(self.frame_4)
        self.parallelogram_perimeter_lcd.setMinimumSize(QtCore.QSize(70, 25))
        self.parallelogram_perimeter_lcd.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parallelogram_perimeter_lcd.setFont(font)
        self.parallelogram_perimeter_lcd.setObjectName("parallelogram_perimeter_lcd")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.parallelogram_perimeter_lcd)
        self.gridLayout_10.addWidget(self.frame_4, 5, 1, 1, 2)
        self.parallelogram_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.parallelogram_lbl.setMinimumSize(QtCore.QSize(300, 300))
        self.parallelogram_lbl.setMaximumSize(QtCore.QSize(300, 16777215))
        self.parallelogram_lbl.setObjectName("parallelogram_lbl")
        self.gridLayout_10.addWidget(self.parallelogram_lbl, 1, 4, 5, 1)
        self.gridLayout_6.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.ParallelogramPage)
        self.gridLayout_7.addWidget(self.stackedWidget, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.mainmenu_btn.hide()
        self.calculate_btn.hide()
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))
        self.mainmenu_btn.setText(_translate("MainWindow", "Back to main menu"))
        self.label_2.setText(_translate("MainWindow", "Calculator"))
        self.Select_btn.setText(_translate("MainWindow", "Select"))
        self.groupBox.setTitle(_translate("MainWindow", "Figures"))
        self.circle_radioButton.setText(_translate("MainWindow", "Circle"))
        self.triangle_radioButton.setText(_translate("MainWindow", "Triangle"))
        self.rectangle_radioButton.setText(_translate("MainWindow", "Rectangle"))
        self.radioButton_4.setText(_translate("MainWindow", "Parallelogram"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Color of Figures"))
        self.radioButton_5.setText(_translate("MainWindow", "Red"))
        self.radioButton_8.setText(_translate("MainWindow", "Yellow"))
        self.radioButton_6.setText(_translate("MainWindow", "Green"))
        self.radioButton_7.setText(_translate("MainWindow", "Blue"))
        self.circle_area_lbl.setText(_translate("MainWindow", "Area:"))
        self.circle_length_lbl.setText(_translate("MainWindow", "Length:"))
        self.label.setText(_translate("MainWindow", "Radius:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Triangle"))
        self.triangle_area_lbl.setText(_translate("MainWindow", "Area:"))
        self.triangle_perimeter_lbl.setText(_translate("MainWindow", "Perimeter:"))
        self.label_5.setText(_translate("MainWindow", "First side:"))
        self.label_6.setText(_translate("MainWindow", "Second side:"))
        self.label_7.setText(_translate("MainWindow", "Third side:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Rectangle"))
        self.rectangle_area_lbl.setText(_translate("MainWindow", "Area:"))
        self.rectangle_perimeter_lbl.setText(_translate("MainWindow", "Perimeter:"))
        self.label_8.setText(_translate("MainWindow", "Second side:"))
        self.label_4.setText(_translate("MainWindow", "First side:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Parallelogram"))
        self.label_3.setText(_translate("MainWindow", "First side:"))
        self.label_11.setText(_translate("MainWindow", "Second side:"))
        self.label_12.setText(_translate("MainWindow", "Angle:"))
        self.parallelogram_area_lbl.setText(_translate("MainWindow", "Area:"))
        self.parallelogram_perimeter_lbl.setText(_translate("MainWindow", "Perimeter:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
