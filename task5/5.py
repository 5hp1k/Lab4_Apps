import sys

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from form import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.view = view = self.graphWidget
        self.curve = view.plot(name="Line")

        self.pushButton.clicked.connect(self.random_plot)

    def random_plot(self):
        np.random.random_sample()
        funcTxt = self.lineEdit.text()

        x = np.linspace(-10, 10, 200)
        y = np.array([])
        for i in x:
            currentFuncStr = funcTxt
            y = np.append(y, eval(currentFuncStr.replace("x", str(i))))

        arr = np.vstack((x, y)).transpose()

        self.curve.setData(arr)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())