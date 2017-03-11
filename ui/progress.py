import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__(parent=None, flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(260, 75, 846, 580)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.home()

    def home(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(130, 225, 600, 50)

        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

        self.close()


def showProgress():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI.setWindowOpacity(0.92)
    GUI.download()

showProgress()
