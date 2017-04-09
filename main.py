from PyQt4.QtCore import Qt
from ui.mainUI import *
import time, sys

# To indicate that our app is a windows application and show icon in task bar
import ctypes
myappid = u'project.analytics.1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# For splash screen ~~
def drawSplash():
    # Create and display the splash screen
    splash_pix = QPixmap('images\splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)  # Splash Screen on top of other windows
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(3)  # Wait for 3 seconds


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    drawSplash()
    # Create main Window
    window = QtGui.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    # Repeat until program terminates
    sys.exit(app.exec_())

