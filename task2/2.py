import sys
import numpy as np

from PyQt5.QtGui import QPixmap, qRgb, QTransform, QImage, qRgba
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.uic.properties import QtCore
from form import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color = "RGB"
        self.angle = 0.0
        self.alpha = 255
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Отображение картинки')

        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)

        self.original_image = QImage(fname[0])
        self.pixmap = QPixmap(self.original_image.copy())
        self.verticalSlider.valueChanged.connect(self.alphaChannel)

    def __show_image(self):
        self.curr_image = self.original_image.copy().convertToFormat(QImage.Format_RGBA8888)

        imgPixelsPtr = self.curr_image.bits()
        imgPixelsPtr.setsize(self.curr_image.byteCount())

        cv_im_in = np.array(imgPixelsPtr, copy=True).reshape(
            self.curr_image.width(), self.curr_image.height(), 4)

        cv_im_in[:, :, 3] = self.alpha

        self.curr_image = QImage(cv_im_in, cv_im_in.shape[1], cv_im_in.shape[0], QImage.Format_RGBA8888).transformed(
            QTransform().rotate(self.angle))
        self.pixmap = QPixmap(self.curr_image)
        self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())

        self.image.setPixmap(self.pixmap)

    def alphaChannel(self):
        alphaNotPrepared = self.verticalSlider.value()
        self.alpha = alphaNotPrepared
        self.__show_image()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())