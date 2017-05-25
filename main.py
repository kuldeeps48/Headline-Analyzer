from PyQt4.QtCore import Qt
from ui.mainUI import *
import time, sys
import socket
import threading

# To indicate that our app is a windows application and show icon in task bar
import ctypes
myappid = u'project.analytics.1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

global ui

today = str(datetime.date.today())
directory = "./data/BestSource/" + today
if not os.path.exists(directory):
    os.makedirs(directory)
file = directory + "/source.txt"

# For splash screen ~~
def drawSplash():
    # Create and display the splash screen
    splash_pix = QPixmap('images\splash.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)  # Splash Screen on top of other windows
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(3)  # Wait for 3 seconds


def ListenService():
    s = socket.socket()  # Create a socket object
    port = 5000  # Reserve a port for our service.
    s.bind(("0.0.0.0", port))  # Bind to the port and all interfaces
    s.listen(1)  # Now wait for client connection.
    while True:
        print("Waiting For A Connection...")
        c, addr = s.accept()  # Establish connection with client.
        print('Got connection from', addr)
        print("Finding Best Source...")
        ui.extractAllButton.click()
        while True:
            with open("./data/done.txt", "r") as f:
                status = f.read()
            if status == "Done":
                print("Got done signal! Responding...")
                break
            else:
                time.sleep(0.5)
        print("Sending reply...")
        greatest = 0
        source_map = {"1": "bbc", "2": "cnn", "3": "googleNews", "4": "nyt", "5": "redditNews",
                      "6": "worldNews", "7": "telegraph", "8": "guardian", "9": "theHindu", "10": "toi"}
        with open(file, "r") as best_source_file:
            for line in best_source_file:
                line_list = line[:-1].split(" ")
                if int(line_list[1]) > greatest:
                    greatest = int(line_list[1])
                    src = line_list[0]

        print("SRC = ", src)
        toSend = source_map[src] + "\n"
        print(toSend)
        c.sendall(toSend.encode('utf-8'))

        with open("./data/done.txt", "w") as f:
            pass
        c.close()  # Close the connection


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    drawSplash()
    # Create main Window
    window = QtGui.QDialog()
    global ui
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    ######################################
    # Remote status file initialize
    with open("./data/Done.txt", "w") as file_open:
        pass
    ######################################
    # Background server listener
    thread = threading.Thread(target=ListenService, args=())
    thread.daemon = True
    thread.start()
    # Repeat until program terminates
    sys.exit(app.exec_())

