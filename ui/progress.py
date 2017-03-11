import sys, time
from PyQt4 import QtGui, QtCore

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
        self.home()

    def home(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(130, 225, 600, 50)

        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.00009
            self.progress.setValue(self.completed)

        time.sleep(0.4)
        self.close()

def showProgress():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI.setWindowOpacity(0.87)
    GUI.download()





showProgress()
