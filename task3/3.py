import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Количество цветов', self)
        self.btn.move(70, 20)
        self.do_paint = False
        self.btn.clicked.connect(self.run)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def run(self):
        self.int_num = QInputDialog.getInt(self, "Определить количество цветов", "Введите количество цветов", 1, 1, 10, 1)

    def draw_flag(self, qp):
        h1 = 60
        h2 = 30
        for i in range(self.int_num[0]):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawRect(30, h2 * i + h1, 120, h2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
