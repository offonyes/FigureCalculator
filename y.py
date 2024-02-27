from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPixmap, QBrush, QPen, QColor, QFont,QPolygonF
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import math

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)

        self.draw_triangle_with_sides(2, 4, "Red")

    def draw_triangle_with_sides(self, a, b, color_name):

        max_coordinate = max(a, b)

        scale_factor = 220 / max_coordinate
        point_A = QPointF(0, 0) * scale_factor + QPointF(20, 50)
        point_B = QPointF(a, 0) * scale_factor + QPointF(20, 50)
        point_C = QPointF(a, b) * scale_factor +QPointF(20, 50)
        point_D = QPointF(0, b) * scale_factor +QPointF(20, 50)

        pixmap = QPixmap(300, 300)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPolygon(QPolygonF([point_A, point_B, point_C, point_D]))
        painter.setBrush(QBrush(QColor(color_name)))

        painter.setPen(QPen(QColor("Black")))
        painter.setFont(QFont("Arial", 10))
        self.draw_text_with_line(painter, point_A, point_B, f"{a:.2f}")
        self.draw_text_with_line(painter, point_B, point_C, f"{b:.2f}")
        self.draw_text_with_line(painter, point_C, point_D, f"{a:.2f}")
        self.draw_text_with_line(painter, point_D, point_A, f"{b:.2f}")

        painter.end()

        self.label.setPixmap(pixmap)

    def draw_text_with_line(self, painter, start_point, end_point, text):
        mid_point = (start_point + end_point) / 2
        painter.setPen(QPen(QColor("Black"), 2, Qt.SolidLine))
        painter.drawLine(start_point, end_point)
        painter.setPen(QPen(QColor("Black")))
        painter.drawText(mid_point + QPointF(5, -5), text)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
