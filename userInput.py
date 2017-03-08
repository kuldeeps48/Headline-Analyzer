''' To display Main page and take user input '''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from posTagging import analyze

class UserInput(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Create Application window
        self.setGeometry(500,300,300,220)
        self.setWindowTitle('Opinion Mining Of News Headlines Using SentiWordNet')
        self.setWindowIcon(QIcon('images/icon.ico'))
        self.setStyleSheet("background-image: url('background.jpg'); background-attachment: fixed")

        #Set tool tips and create analize button
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Choose one of the option to begin.')
        btn = QPushButton('Demo', self)
        btn.setToolTip('<b><i>Enter a headline to begin analysis</i></b>')
        btn.resize(btn.sizeHint())
        btn.move(120,80)
        btn.clicked.connect(lambda : analyze())

        self.show()

    def closeEvent(self, event):
        # Show exit confirmation
        reply = QMessageBox.question(self, 'Message', 'Exit the program?', QMessageBox.Yes | QMessageBox.No,\
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
