# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QLCDNumber,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 490)
        MainWindow.setMinimumSize(QSize(640, 490))
        MainWindow.setMaximumSize(QSize(640, 490))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.calculate_btn = QPushButton(self.centralwidget)
        self.calculate_btn.setObjectName(u"calculate_btn")

        self.gridLayout_7.addWidget(self.calculate_btn, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 5, 0, 1, 4)

        self.mainmenu_btn = QPushButton(self.centralwidget)
        self.mainmenu_btn.setObjectName(u"mainmenu_btn")

        self.gridLayout_7.addWidget(self.mainmenu_btn, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.MainPage.setStyleSheet(u"            QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 2px solid rgba(0, 0, 0, 190);\n"
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
        self.gridLayout = QGridLayout(self.MainPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 2, 0, 1, 5)

        self.label_2 = QLabel(self.MainPage)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 3)

        self.Select_btn = QPushButton(self.MainPage)
        self.Select_btn.setObjectName(u"Select_btn")

        self.gridLayout.addWidget(self.Select_btn, 5, 1, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 3, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 4, 1, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 3, 1, 1)

        self.groupBox = QGroupBox(self.MainPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(140, 130))
        self.groupBox.setMaximumSize(QSize(140, 150))
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.circle_radioButton = QRadioButton(self.groupBox)
        self.FiguresButtonGroup = QButtonGroup(MainWindow)
        self.FiguresButtonGroup.setObjectName(u"FiguresButtonGroup")
        self.FiguresButtonGroup.addButton(self.circle_radioButton)
        self.circle_radioButton.setObjectName(u"circle_radioButton")
        font1 = QFont()
        font1.setPointSize(12)
        self.circle_radioButton.setFont(font1)
        self.circle_radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.circle_radioButton)

        self.triangle_radioButton = QRadioButton(self.groupBox)
        self.FiguresButtonGroup.addButton(self.triangle_radioButton)
        self.triangle_radioButton.setObjectName(u"triangle_radioButton")
        self.triangle_radioButton.setFont(font1)

        self.verticalLayout.addWidget(self.triangle_radioButton)

        self.rectangle_radioButton = QRadioButton(self.groupBox)
        self.FiguresButtonGroup.addButton(self.rectangle_radioButton)
        self.rectangle_radioButton.setObjectName(u"rectangle_radioButton")
        self.rectangle_radioButton.setFont(font1)

        self.verticalLayout.addWidget(self.rectangle_radioButton)

        self.radioButton_4 = QRadioButton(self.groupBox)
        self.FiguresButtonGroup.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton_4)


        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.MainPage)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(140, 130))
        self.groupBox_2.setMaximumSize(QSize(140, 150))
        self.groupBox_2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.ColorButtonGroup = QButtonGroup(MainWindow)
        self.ColorButtonGroup.setObjectName(u"ColorButtonGroup")
        self.ColorButtonGroup.addButton(self.radioButton_5)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font1)
        self.radioButton_5.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_5)

        self.radioButton_8 = QRadioButton(self.groupBox_2)
        self.ColorButtonGroup.addButton(self.radioButton_8)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_8)

        self.radioButton_6 = QRadioButton(self.groupBox_2)
        self.ColorButtonGroup.addButton(self.radioButton_6)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox_2)
        self.ColorButtonGroup.addButton(self.radioButton_7)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.radioButton_7)


        self.gridLayout.addWidget(self.groupBox_2, 3, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.MainPage)
        self.CirclePage = QWidget()
        self.CirclePage.setObjectName(u"CirclePage")
        self.gridLayout_2 = QGridLayout(self.CirclePage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.CirclePage)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(70, 25))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(True)
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setStyleSheet(u"            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.groupBox_3.setTitle(u"Circle")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 3, 8, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 2, 1, 6)

        self.radius_spinbox = QDoubleSpinBox(self.groupBox_3)
        self.radius_spinbox.setObjectName(u"radius_spinbox")
        self.radius_spinbox.setMinimumSize(QSize(120, 25))
        self.radius_spinbox.setMaximumSize(QSize(150, 30))
        font3 = QFont()
        font3.setPointSize(14)
        self.radius_spinbox.setFont(font3)
        self.radius_spinbox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.radius_spinbox, 2, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 3, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 5, 7, 1, 1)

        self.Circle_lbl = QLabel(self.groupBox_3)
        self.Circle_lbl.setObjectName(u"Circle_lbl")
        self.Circle_lbl.setMinimumSize(QSize(300, 300))
        self.Circle_lbl.setMaximumSize(QSize(600, 600))
        self.Circle_lbl.setSizeIncrement(QSize(50, 10))
        self.Circle_lbl.setStyleSheet(u"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 150px; \n"
"")

        self.gridLayout_4.addWidget(self.Circle_lbl, 2, 7, 3, 1)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(190, 50))
        self.frame.setMaximumSize(QSize(240, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.circle_area_lbl = QLabel(self.frame)
        self.circle_area_lbl.setObjectName(u"circle_area_lbl")
        self.circle_area_lbl.setMinimumSize(QSize(70, 25))
        self.circle_area_lbl.setMaximumSize(QSize(90, 30))
        font4 = QFont()
        font4.setPointSize(15)
        self.circle_area_lbl.setFont(font4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.circle_area_lbl)

        self.circle_area_lcd = QLCDNumber(self.frame)
        self.circle_area_lcd.setObjectName(u"circle_area_lcd")
        self.circle_area_lcd.setMinimumSize(QSize(120, 25))
        self.circle_area_lcd.setMaximumSize(QSize(150, 30))
        self.circle_area_lcd.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.circle_area_lcd)

        self.circle_length_lbl = QLabel(self.frame)
        self.circle_length_lbl.setObjectName(u"circle_length_lbl")
        self.circle_length_lbl.setMinimumSize(QSize(70, 25))
        self.circle_length_lbl.setMaximumSize(QSize(90, 30))
        self.circle_length_lbl.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.circle_length_lbl)

        self.circle_length_lcd = QLCDNumber(self.frame)
        self.circle_length_lcd.setObjectName(u"circle_length_lcd")
        self.circle_length_lcd.setMinimumSize(QSize(120, 25))
        self.circle_length_lcd.setMaximumSize(QSize(150, 30))
        self.circle_length_lcd.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.circle_length_lcd)


        self.gridLayout_4.addWidget(self.frame, 4, 3, 1, 3)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 25))
        self.label.setMaximumSize(QSize(90, 30))
        self.label.setFont(font4)

        self.gridLayout_4.addWidget(self.label, 2, 3, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.CirclePage)
        self.TrianglePage = QWidget()
        self.TrianglePage.setObjectName(u"TrianglePage")
        self.gridLayout_3 = QGridLayout(self.TrianglePage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_4 = QGroupBox(self.TrianglePage)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font2)
        self.groupBox_4.setStyleSheet(u"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 8, 4, 1, 1)

        self.frame_2 = QFrame(self.groupBox_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(190, 50))
        self.frame_2.setMaximumSize(QSize(240, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.triangle_area_lbl = QLabel(self.frame_2)
        self.triangle_area_lbl.setObjectName(u"triangle_area_lbl")
        self.triangle_area_lbl.setMinimumSize(QSize(100, 25))
        self.triangle_area_lbl.setMaximumSize(QSize(120, 30))
        self.triangle_area_lbl.setFont(font4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.triangle_area_lbl)

        self.triangle_area_lcd = QLCDNumber(self.frame_2)
        self.triangle_area_lcd.setObjectName(u"triangle_area_lcd")
        self.triangle_area_lcd.setMinimumSize(QSize(70, 25))
        self.triangle_area_lcd.setMaximumSize(QSize(120, 30))
        self.triangle_area_lcd.setFont(font3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.triangle_area_lcd)

        self.triangle_perimeter_lbl = QLabel(self.frame_2)
        self.triangle_perimeter_lbl.setObjectName(u"triangle_perimeter_lbl")
        self.triangle_perimeter_lbl.setMinimumSize(QSize(100, 25))
        self.triangle_perimeter_lbl.setMaximumSize(QSize(120, 30))
        self.triangle_perimeter_lbl.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.triangle_perimeter_lbl)

        self.triangle_perimeter_lcd = QLCDNumber(self.frame_2)
        self.triangle_perimeter_lcd.setObjectName(u"triangle_perimeter_lcd")
        self.triangle_perimeter_lcd.setMinimumSize(QSize(70, 25))
        self.triangle_perimeter_lcd.setMaximumSize(QSize(120, 30))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.triangle_perimeter_lcd)


        self.gridLayout_8.addWidget(self.frame_2, 7, 1, 1, 2)

        self.triangle_ds = QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds.setObjectName(u"triangle_ds")
        self.triangle_ds.setMinimumSize(QSize(90, 25))
        self.triangle_ds.setMaximumSize(QSize(120, 30))
        self.triangle_ds.setFont(font1)
        self.triangle_ds.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.triangle_ds, 4, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 25))
        self.label_5.setMaximumSize(QSize(120, 30))
        font5 = QFont()
        font5.setPointSize(13)
        self.label_5.setFont(font5)

        self.gridLayout_8.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 25))
        self.label_6.setMaximumSize(QSize(120, 30))
        self.label_6.setFont(font5)

        self.gridLayout_8.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 25))
        self.label_7.setMaximumSize(QSize(120, 30))
        self.label_7.setFont(font5)

        self.gridLayout_8.addWidget(self.label_7, 4, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_9, 6, 5, 1, 1)

        self.triangle_ds_3 = QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds_3.setObjectName(u"triangle_ds_3")
        self.triangle_ds_3.setMinimumSize(QSize(90, 25))
        self.triangle_ds_3.setMaximumSize(QSize(120, 30))
        self.triangle_ds_3.setFont(font1)
        self.triangle_ds_3.setLayoutDirection(Qt.LeftToRight)
        self.triangle_ds_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.triangle_ds_3, 1, 2, 1, 1)

        self.triangle_ds_2 = QDoubleSpinBox(self.groupBox_4)
        self.triangle_ds_2.setObjectName(u"triangle_ds_2")
        self.triangle_ds_2.setMinimumSize(QSize(90, 25))
        self.triangle_ds_2.setMaximumSize(QSize(120, 30))
        self.triangle_ds_2.setFont(font1)
        self.triangle_ds_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.triangle_ds_2, 2, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 6, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_8, 6, 0, 1, 1)

        self.triangle_lbl = QLabel(self.groupBox_4)
        self.triangle_lbl.setObjectName(u"triangle_lbl")
        self.triangle_lbl.setMinimumSize(QSize(300, 300))
        self.triangle_lbl.setMaximumSize(QSize(900, 900))
        self.triangle_lbl.setSizeIncrement(QSize(50, 10))
        self.triangle_lbl.setStyleSheet(u"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 150px; \n"
"")

        self.gridLayout_8.addWidget(self.triangle_lbl, 1, 4, 7, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 0, 1, 1, 4)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.TrianglePage)
        self.RectanglePage = QWidget()
        self.RectanglePage.setObjectName(u"RectanglePage")
        self.gridLayout_5 = QGridLayout(self.RectanglePage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_5 = QGroupBox(self.RectanglePage)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font2)
        self.groupBox_5.setStyleSheet(u"            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_3 = QFrame(self.groupBox_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(190, 50))
        self.frame_3.setMaximumSize(QSize(240, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.rectangle_area_lbl = QLabel(self.frame_3)
        self.rectangle_area_lbl.setObjectName(u"rectangle_area_lbl")
        self.rectangle_area_lbl.setMinimumSize(QSize(100, 25))
        self.rectangle_area_lbl.setMaximumSize(QSize(120, 30))
        self.rectangle_area_lbl.setFont(font4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.rectangle_area_lbl)

        self.rectangle_perimeter_lbl = QLabel(self.frame_3)
        self.rectangle_perimeter_lbl.setObjectName(u"rectangle_perimeter_lbl")
        self.rectangle_perimeter_lbl.setMinimumSize(QSize(100, 25))
        self.rectangle_perimeter_lbl.setMaximumSize(QSize(120, 30))
        self.rectangle_perimeter_lbl.setFont(font4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.rectangle_perimeter_lbl)

        self.rectangle_area_lcd = QLCDNumber(self.frame_3)
        self.rectangle_area_lcd.setObjectName(u"rectangle_area_lcd")
        self.rectangle_area_lcd.setMinimumSize(QSize(70, 25))
        self.rectangle_area_lcd.setMaximumSize(QSize(120, 30))
        self.rectangle_area_lcd.setFont(font3)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.rectangle_area_lcd)

        self.rectangle_perimeter_lcd = QLCDNumber(self.frame_3)
        self.rectangle_perimeter_lcd.setObjectName(u"rectangle_perimeter_lcd")
        self.rectangle_perimeter_lcd.setMinimumSize(QSize(70, 25))
        self.rectangle_perimeter_lcd.setMaximumSize(QSize(120, 30))
        self.rectangle_perimeter_lcd.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.rectangle_perimeter_lcd)


        self.gridLayout_9.addWidget(self.frame_3, 5, 1, 1, 2)

        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 25))
        self.label_8.setMaximumSize(QSize(120, 30))
        self.label_8.setFont(font5)

        self.gridLayout_9.addWidget(self.label_8, 3, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_13, 6, 4, 1, 1)

        self.rectangle_ds = QDoubleSpinBox(self.groupBox_5)
        self.rectangle_ds.setObjectName(u"rectangle_ds")
        self.rectangle_ds.setMinimumSize(QSize(90, 25))
        self.rectangle_ds.setMaximumSize(QSize(120, 30))
        self.rectangle_ds.setFont(font1)

        self.gridLayout_9.addWidget(self.rectangle_ds, 1, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 4, 5, 1, 1)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 25))
        self.label_4.setMaximumSize(QSize(120, 30))
        self.label_4.setFont(font5)

        self.gridLayout_9.addWidget(self.label_4, 1, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_12, 4, 3, 1, 1)

        self.rectangle_ds_3 = QDoubleSpinBox(self.groupBox_5)
        self.rectangle_ds_3.setObjectName(u"rectangle_ds_3")
        self.rectangle_ds_3.setMinimumSize(QSize(90, 25))
        self.rectangle_ds_3.setMaximumSize(QSize(120, 30))
        self.rectangle_ds_3.setFont(font1)

        self.gridLayout_9.addWidget(self.rectangle_ds_3, 3, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_11, 4, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(525, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 0, 1, 1, 4)

        self.Rectangle_lbl = QLabel(self.groupBox_5)
        self.Rectangle_lbl.setObjectName(u"Rectangle_lbl")
        self.Rectangle_lbl.setMinimumSize(QSize(300, 300))
        self.Rectangle_lbl.setMaximumSize(QSize(300, 300))
        self.Rectangle_lbl.setStyleSheet(u"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 150px; \n"
"")

        self.gridLayout_9.addWidget(self.Rectangle_lbl, 1, 4, 5, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.RectanglePage)
        self.ParallelogramPage = QWidget()
        self.ParallelogramPage.setObjectName(u"ParallelogramPage")
        self.gridLayout_6 = QGridLayout(self.ParallelogramPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_6 = QGroupBox(self.ParallelogramPage)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setStyleSheet(u"            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                padding: 0 3px;\n"
"            } \n"
"QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 3px solid gray;\n"
"                margin-top: 10px;\n"
"            }")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_14, 4, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_13, 4, 3, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_16, 4, 5, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_15, 6, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 25))
        self.label_3.setMaximumSize(QSize(120, 30))
        self.label_3.setFont(font5)

        self.gridLayout_10.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 25))
        self.label_11.setMaximumSize(QSize(120, 30))
        self.label_11.setFont(font5)

        self.gridLayout_10.addWidget(self.label_11, 2, 1, 1, 1)

        self.parallelogran_ds = QDoubleSpinBox(self.groupBox_6)
        self.parallelogran_ds.setObjectName(u"parallelogran_ds")
        self.parallelogran_ds.setMinimumSize(QSize(90, 25))
        self.parallelogran_ds.setMaximumSize(QSize(120, 30))
        self.parallelogran_ds.setFont(font1)

        self.gridLayout_10.addWidget(self.parallelogran_ds, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 25))
        self.label_12.setMaximumSize(QSize(120, 30))
        self.label_12.setFont(font5)

        self.gridLayout_10.addWidget(self.label_12, 3, 1, 1, 1)

        self.parallelogran_ds_2 = QDoubleSpinBox(self.groupBox_6)
        self.parallelogran_ds_2.setObjectName(u"parallelogran_ds_2")
        self.parallelogran_ds_2.setMinimumSize(QSize(90, 25))
        self.parallelogran_ds_2.setMaximumSize(QSize(120, 30))
        self.parallelogran_ds_2.setFont(font1)

        self.gridLayout_10.addWidget(self.parallelogran_ds_2, 2, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_14, 0, 1, 1, 4)

        self.parallelogran_angle_ds = QDoubleSpinBox(self.groupBox_6)
        self.parallelogran_angle_ds.setObjectName(u"parallelogran_angle_ds")
        self.parallelogran_angle_ds.setMinimumSize(QSize(90, 25))
        self.parallelogran_angle_ds.setMaximumSize(QSize(120, 30))
        self.parallelogran_angle_ds.setFont(font1)
        self.parallelogran_angle_ds.setMaximum(180.990000000000009)

        self.gridLayout_10.addWidget(self.parallelogran_angle_ds, 3, 2, 1, 1)

        self.frame_4 = QFrame(self.groupBox_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(190, 50))
        self.frame_4.setMaximumSize(QSize(240, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.parallelogran_area_lbl = QLabel(self.frame_4)
        self.parallelogran_area_lbl.setObjectName(u"parallelogran_area_lbl")
        self.parallelogran_area_lbl.setMinimumSize(QSize(100, 25))
        self.parallelogran_area_lbl.setMaximumSize(QSize(120, 30))
        self.parallelogran_area_lbl.setFont(font4)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.parallelogran_area_lbl)

        self.parallelogran_area_lcd = QLCDNumber(self.frame_4)
        self.parallelogran_area_lcd.setObjectName(u"parallelogran_area_lcd")
        self.parallelogran_area_lcd.setMinimumSize(QSize(70, 25))
        self.parallelogran_area_lcd.setMaximumSize(QSize(120, 30))
        self.parallelogran_area_lcd.setFont(font3)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.parallelogran_area_lcd)

        self.parallelogran_perimeter_lbl = QLabel(self.frame_4)
        self.parallelogran_perimeter_lbl.setObjectName(u"parallelogran_perimeter_lbl")
        self.parallelogran_perimeter_lbl.setFont(font4)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.parallelogran_perimeter_lbl)

        self.parallelogran_perimeter_lcd = QLCDNumber(self.frame_4)
        self.parallelogran_perimeter_lcd.setObjectName(u"parallelogran_perimeter_lcd")
        self.parallelogran_perimeter_lcd.setMinimumSize(QSize(70, 25))
        self.parallelogran_perimeter_lcd.setMaximumSize(QSize(120, 30))
        self.parallelogran_perimeter_lcd.setFont(font3)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.parallelogran_perimeter_lcd)


        self.gridLayout_10.addWidget(self.frame_4, 5, 1, 1, 2)

        self.parallelogran_lbl = QLabel(self.groupBox_6)
        self.parallelogran_lbl.setObjectName(u"parallelogran_lbl")
        self.parallelogran_lbl.setMinimumSize(QSize(300, 300))
        self.parallelogran_lbl.setMaximumSize(QSize(300, 16777215))
        self.parallelogran_lbl.setStyleSheet(u"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 150px; \n"
"")

        self.gridLayout_10.addWidget(self.parallelogran_lbl, 1, 4, 5, 1)


        self.gridLayout_6.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.ParallelogramPage)

        self.gridLayout_7.addWidget(self.stackedWidget, 1, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calculate_btn.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.mainmenu_btn.setText(QCoreApplication.translate("MainWindow", u"Back to main menu", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.Select_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Figures", None))
        self.circle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.triangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.rectangle_radioButton.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Parallelogram", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color of Figures", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Circle_lbl.setText(QCoreApplication.translate("MainWindow", u" CIRCLe", None))
        self.circle_area_lbl.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.circle_length_lbl.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Radius:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.triangle_area_lbl.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.triangle_perimeter_lbl.setText(QCoreApplication.translate("MainWindow", u"Perimeter:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First side:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Second side:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Third side:", None))
        self.triangle_lbl.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.rectangle_area_lbl.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.rectangle_perimeter_lbl.setText(QCoreApplication.translate("MainWindow", u"Perimeter:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Second side:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"First side:", None))
        self.Rectangle_lbl.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Parallelogram", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"First side:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Second side:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Angle:", None))
        self.parallelogran_area_lbl.setText(QCoreApplication.translate("MainWindow", u"Area:", None))
        self.parallelogran_perimeter_lbl.setText(QCoreApplication.translate("MainWindow", u"Perimeter:", None))
        self.parallelogran_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

