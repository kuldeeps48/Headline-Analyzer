import sys, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from userInput import UserInput

class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')

    def update_ui(self):
        self.browser.append(self.lineedit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap('images\splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    form = UserInput()
    form.show()
    splash.finish(form)
    app.exec_()