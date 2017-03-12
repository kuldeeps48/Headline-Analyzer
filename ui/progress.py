import sys, time
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import *

DEFAULT_STYLE = """QProgressBar{border: 2px solid white;
                                border-radius: 5px;
                                text-align: center}
                   QMainWindow {background-color:black;}"""


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__(parent=None, flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(260, 75, 846, 580)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.setStyleSheet(DEFAULT_STYLE)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.createItems()

    def createItems(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(130, 225, 600, 50)

        # QLabel


        self.show()

    def download(self):
        self.extractProgress = 0
        while self.extractProgress < 100:
            self.extractProgress += 0.0001
            self.progress.setValue(self.extractProgress)

        time.sleep(0.4)

        self.analyseProgress = 0
        while self.analyseProgress < 100:
            self.analyseProgress += 0.00003
            self.progress.setValue(self.analyseProgress)

        time.sleep(0.4)
        self.close()


def showProgress():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI.setWindowOpacity(0.87)
    GUI.download()
    app.processEvents()

if __name__ == '__main__':
    showProgress()
