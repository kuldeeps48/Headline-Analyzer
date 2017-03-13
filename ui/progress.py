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

        # Label
        self.label = QtGui.QLabel("Fetching News Headlines From Web", self)
        self.label.setGeometry(QtCore.QRect(85, 165, 700, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {color:white;}")
        self.font = QtGui.QFont()
        self.font.setFamily("Vivaldi")
        self.font.setPointSize(26)
        self.font.setBold(False)
        self.font.setWeight(75)
        self.label.setFont(self.font)

        self.createItems()
        self.show()

    def createItems(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(130, 225, 600, 50)
        self.setWindowOpacity(0.9)


    def download(self):
        self.extractProgress = 0
        while self.extractProgress < 100:
            self.extractProgress += 0.0001
            self.progress.setValue(self.extractProgress)

        time.sleep(0.4)

        self.analyseProgress = 0
        self.label.setText("Analyzing Fetched Headlines")
        while self.analyseProgress < 100:
            self.analyseProgress += 0.00003
            self.progress.setValue(self.analyseProgress)

        time.sleep(0.4)
        self.close()


def showProgress():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI.download()
    app.processEvents()

if __name__ == '__main__':
    showProgress()
