from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
from PyQt5.QtGui import QPainter, QColor
import sys
from form import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.color = "red"
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Смайлик')
        self.slider.valueChanged.connect(self.update)
        self.peakColorButton.clicked.connect(self.peakColor)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.scale(self.slider.value() / 100, self.slider.value() / 100)
        self.draw_smile(qp)
        qp.end()

    def draw_smile(self, qp):
        qp.setPen(QColor(self.color))
        qp.drawEllipse(30, 30, 200, 200)
        qp.drawEllipse(70, 70, 40, 40)
        qp.drawEllipse(145, 70, 40, 40)
        qp.drawArc(QRectF(80.0, 100.0, 100.0, 90.0), 220 * 16, 100 * 16)

    def peakColor(self):
        dlg = QColorDialog(self)
        if self.color:
            dlg.setCurrentColor(QColor(self.color))

        if dlg.exec_():
            self.color = dlg.currentColor().name()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())