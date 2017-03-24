from PyQt4.QtCore import Qt
from ui.mainUI import *
import time, sys


# For splash screen ~~
def drawSplash():
    # Create and display the splash screen
    splash_pix = QPixmap('images\splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    # Simulate something that takes time
    time.sleep(2)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # Splash screen for 2 seconds
    drawSplash()
    # Create main Window
    window = QtGui.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

