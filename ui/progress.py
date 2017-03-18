import time
from PyQt4 import QtGui, QtCore

DEFAULT_STYLE = """QProgressBar{border: 1px solid black;
                                border-radius: 5px;
                                text-align: center;
                                background-color: darkgreen;
                                width: 10px;
                                margin: 1px;}
                   QMainWindow {background-color:black;}"""


class Loading(QtGui.QMainWindow):
    def __init__(self):
        super(Loading, self).__init__(parent=None, flags=QtCore.Qt.FramelessWindowHint)
        self.setGeometry(260, 75, 846, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(DEFAULT_STYLE)
        self.setWindowOpacity(0.7)
        # self.setWindowFlags(QtCore.Qt.Tool) # To prevent taskbar thing from appearing
        # Label
        self.label = QtGui.QLabel("Fetching News Headlines From Web", self)
        self.label.setGeometry(QtCore.QRect(85, 525, 700, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {color: white;}")
        self.font = QtGui.QFont()
        self.font.setFamily("Century Gothic")
        self.font.setPointSize(12)
        self.font.setBold(False)
        self.font.setWeight(75)
        self.label.setFont(self.font)
        # Create Items and show
        self.createItems()
        self.show()

    def createItems(self):
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(1, 562, 845, 19)

    def download(self,e):
        self.extractProgress = 0
        while not e.is_set():
            if self.extractProgress > 99:
                continue
            self.extractProgress += 0.0001
            self.progress.setValue(self.extractProgress)

        self.progress.setValue(100)
        time.sleep(0.5)

        self.label.setText("Analyzing Fetched Headlines")
        QtGui.QProgressBar.reset(self.progress)
        self.analyseProgress = 0
        while not e.is_set():
            if self.analyseProgress > 98:
                continue
            self.analyseProgress += 0.0001
            self.progress.setValue(self.analyseProgress)

        self.progress.setValue(100)
        time.sleep(0.5)
        self.close()

"""
~~~~~~For testing only, remove synchronization before running just progress.py~~~~~~
def showProgress():
    app = QtGui.QApplication(sys.argv)
    GUI = Loading()
    GUI.download()
    app.processEvents()

if __name__ == "__main__":
    showProgress()
"""