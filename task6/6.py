import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtMultimedia


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)

        self.C.clicked.connect(self.playNote)
        self.D.clicked.connect(self.playNote)
        self.E.clicked.connect(self.playNote)
        self.F.clicked.connect(self.playNote)
        self.G.clicked.connect(self.playNote)
        self.A.clicked.connect(self.playNote)
        self.B.clicked.connect(self.playNote)

    def playNote(self):
        self.load_file(f'Samples/{self.sender().objectName()}3.mp3')
        self.player.play()

    def load_file(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
