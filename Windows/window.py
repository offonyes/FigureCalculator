from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Windows.MainWindow import Ui_MainWindow
from math import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Select_btn.clicked.connect(self.select_shape)
        self.mainmenu_btn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MainPage))
        self.calculate_btn.clicked.connect(lambda: self.calculate(self.FiguresButtonGroup.checkedButton().text(), self.ColorButtonGroup.checkedButton().text()))

    def calculate(self, state, color):
        if state == "Circle":
            r = self.circle_spinbox.value()
            area_answer = pi * r ** 2
            length_answer = 2 * pi * r
            self.circle_area_lcd.display(area_answer)
            self.circle_length_lcd.display(length_answer)
        elif state == "Triangle":
            a = self.triangle_ds.value()
            b = self.triangle_ds_2.value()
            c = self.triangle_ds_3.value()
            if max(a,b,c) < (a + b + c - max(a,b,c)):
                self.draw_triangle(a, b, c, color)
                s = (a + b + c)/2
                area_answer = sqrt((s-a)*(s-b)*(s-c))
                self.triangle_area_lcd.display(area_answer)
                self.triangle_perimeter_lcd.display(a + b + c)
            else:
                QMessageBox.critical(self, "Error", "Such triangle cant exist")
        elif state == "Rectangle":
            a = self.rectangle_ds.value()
            b = self.rectangle_ds_2.value()
            self.draw_rectangle(a, b, color)
            self.rectangle_area_lcd.display(a*b)
            self.rectangle_perimeter_lcd.display((a+b)*2)
        else:
            a = self.parallelogram_ds.value()
            b = self.parallelogram_ds_2.value()
            angle_a = self.parallelogram_angle_ds.value()
            self.parallelogram_area_lcd.display(a*b*sin(angle_a))
            self.parallelogram_perimeter_lcd.display((a+b)*2)
    
    def select_shape(self):
        self.mainmenu_btn.show()
        self.calculate_btn.show()
        shape_name = self.FiguresButtonGroup.checkedButton().text()
        self.stackedWidget.setCurrentWidget(getattr(self, f"{shape_name}Page", self.MainPage))

        if shape_name == "Circle":
            self.paint_circle(self.ColorButtonGroup.checkedButton().text(),self.circle_spinbox.value())
            self.circle_spinbox.valueChanged.connect(lambda: self.paint_circle(self.ColorButtonGroup.checkedButton().text(),self.circle_spinbox.value()))  

    def draw_rectangle(self, a, b, color_name):
        max_coordinate = max(a, b)

        scale_factor = 220 / max_coordinate
        point_A = QPointF(0, 0) * scale_factor + QPointF(20, 50)
        point_B = QPointF(a, 0) * scale_factor + QPointF(20, 50)
        point_C = QPointF(a, b) * scale_factor + QPointF(20, 50)
        point_D = QPointF(0, b) * scale_factor + QPointF(20, 50)

        pixmap = QPixmap(300, 300)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(color_name)))
        painter.drawPolygon(QPolygonF([point_A, point_B, point_C, point_D]))

        painter.setPen(QPen(QColor("Black")))
        painter.setFont(QFont("Arial", 10))
        self.draw_text_with_line(painter, point_A, point_B, f"{a:.2f}")
        self.draw_text_with_line(painter, point_B, point_C, f"{b:.2f}")
        self.draw_text_with_line(painter, point_C, point_D, f"{a:.2f}")
        self.draw_text_with_line(painter, point_D, point_A, f"{b:.2f}")

        painter.end()

        self.Rectangle_lbl.setPixmap(pixmap)
    def draw_triangle(self, a, b, c, color_name):
        angle_A = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
        b_coords = c * cos(radians(angle_A))
        c_coords = c * sin(radians(angle_A))

        max_coordinate = max(a, b_coords, c_coords)

        scale_factor = 220 / max_coordinate
        point_A = QPointF(0, 0) * scale_factor + QPointF(20, 50)
        point_B = QPointF(a, 0) * scale_factor + QPointF(20, 50)
        point_C = QPointF(b_coords, c_coords) * scale_factor + QPointF(20, 50)

        pixmap = QPixmap(300, 300)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(QColor(color_name)))
        painter.drawPolygon(QPolygonF([point_A, point_B, point_C]))

        painter.setPen(QPen(QColor("Black")))
        painter.setFont(QFont("Arial", 10))
        self.draw_text_with_line(painter, point_A, point_B, f"{a:.2f}")
        self.draw_text_with_line(painter, point_B, point_C, f"{b:.2f}")
        self.draw_text_with_line(painter, point_C, point_A, f"{c:.2f}")

        painter.end()
        self.triangle_lbl.setPixmap(pixmap)








    def paint_circle(self, color, r):
        size = self.Circle_lbl.size()
        pixmap = QPixmap(size)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)  
        radius = int(min(size.width(), size.height()) / 2 - 10)
        if r < 5:
            radius = 50
        elif r >= 5 and r <=14:
            radius = int(r)*10
        center = QPoint(int(size.width()/2), int(size.height()/2))
        painter.setBrush(QBrush(QColor(f"{color}")))  
        painter.drawEllipse(center, radius, radius)
        self.draw_text_with_line(painter, center, QPoint(int(size.width()/2) + radius, int(size.height()/2)), f"{r:.2f}")
        painter.end()
        self.Circle_lbl.setPixmap(pixmap)   

    def draw_text_with_line(self, painter, start_point, end_point, text):
        mid_point = (start_point + end_point) / 2
        painter.setPen(QPen(QColor("Black"), 2, Qt.SolidLine))
        painter.drawLine(start_point, end_point)
        painter.setPen(QPen(QColor("Black")))
        font = QFont("Arial", 18)  
        painter.setFont(font)
        painter.drawText(mid_point + QPointF(5, -5), text)