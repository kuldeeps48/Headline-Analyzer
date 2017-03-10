''' To display Main page and take user input '''

import sys, time, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *



def open():
    os.system("python posTagging.py")



class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')

    def update_ui(self):
        self.browser.append(self.lineedit.text())



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
        btn.clicked.connect(lambda: open())
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

def drawMainUI():
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('images\splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()


    # Simulate something that takes time
    time.sleep(2)

    form = UserInput()
    form.show()
    splash.finish(form)
    app.processEvents()
    app.exec_()