import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QColor, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)

        self.setFixedSize(600, 425)
        self.loadImage()

        self.rotRightButton.clicked.connect(lambda: self.rotate(90))
        self.rotLeftButton.clicked.connect(lambda: self.rotate(-90))
        self.colorButton.clicked.connect(self.changeColor)

    def loadImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)
        self.pixmap = QPixmap(fname[0])
        self.image = QLabel(self)
        self.image.move(150, 5)
        self.image.resize(306, 313)
        self.image.setPixmap(self.pixmap)

    def changeColor(self):
        if self.image is not None:
            image = self.pixmap.toImage()
            for x in range(image.width()):
                for y in range(image.height()):
                    color = QColor(image.pixel(x, y))
                    image.setPixel(x, y, QColor(color.green(), 0, 0).rgb())

            self.image.setPixmap(QPixmap.fromImage(image))

    def rotate(self, angle):
        if self.pixmap is not None:
            transform = QTransform().rotate(angle)
            self.pixmap = self.pixmap.transformed(transform)
            self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
