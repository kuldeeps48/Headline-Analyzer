# -*- coding: utf-8 -*-
import multiprocessing
import subprocess
import images.mainuiImages  # image resources for mainUI
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import extractorRunner
from ui.progress import Loading
from ui.customLoading import ImagePlayer
import datetime, os
from multiprocessing.dummy import Pool as ThreadPool
from itertools import repeat

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

MainW = 0  # Global reference to our program


def getIpAddress():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


class Ui_window(object):
    # Function to call when a newspaper is selected
    def selected_extractor(self):
        self.customScoreLabel.hide()  # remove custom score label if present
        QApplication.processEvents()  # display any graphics(UI) change

        button_to_name = {"pushButton": "times of india", "pushButton_2": "the hindu", "pushButton_3": "guardian",
                          "pushButton_4": "new york times", "pushButton_5": "google news", "pushButton_6": "cnn",
                          "pushButton_7": "reddit news", "pushButton_8": "reddit world news",
                          "pushButton_9": "telegraph",
                          "pushButton_10": "bbc"}

        sending_button = self.MainWindow.sender()  # Find which button was clicked
        name = button_to_name[str(sending_button.objectName())]  # Get the button's defined name

        # To synchronize progress bar
        e = multiprocessing.Event()
        queue = multiprocessing.Queue()  # To get score file from threaded process
        p = multiprocessing.Process(target=extractorRunner.runScrapper, args=(name, e, queue)).start()
        # create loading screen
        GUI = Loading()
        xPos = MainW.geometry().topLeft().x()
        yPos = MainW.geometry().topLeft().y()
        GUI.setGeometry(xPos, yPos, 846, 582)  # Set it on top of mainUI window
        GUI.download(e)  # Start progress bar with sync

        outputFile = queue.get()

        # Wait Label
        self.buildingOutputLabel.show()
        QApplication.processEvents()
        # Build and Show output, wait for it to be closed
        outputProcess = subprocess.Popen("python -m ui.output " + outputFile + " " + name.replace(" ", "-"))
        outputProcess.wait()
        self.buildingOutputLabel.hide()
        QApplication.processEvents()  # Progress GUI events
        while os.path.exists("./data/dateSelected.txt"):
            print("Found a date with no data. Beginning fetch.")
            with open("./data/dateSelected.txt") as f:
                line = f.readline()
                name = line[:-11]
                date = line[-10:]
                year = date[:4]
                month = date[5:7]
                day = date[8:]
            os.remove("./data/dateSelected.txt")
            if not os.path.exists("./data/dateSelected.txt"):
                print("Removed the date selected file. Processing it.")

            # To synchronize progress bar
            e = multiprocessing.Event()
            queue = multiprocessing.Queue()  # To get score file from threaded process
            p = multiprocessing.Process(target=extractorRunner.runScrapperDate, args=(name, e, queue, year, month, day)).start()
            # create loading screen
            GUI = Loading()
            xPos = MainW.geometry().topLeft().x()
            yPos = MainW.geometry().topLeft().y()
            GUI.setGeometry(xPos, yPos, 846, 582)  # Set it on top of mainUI window
            GUI.download(e)  # Start progress bar with sync
            outputFile = queue.get()
            # Wait Label
            self.buildingOutputLabel.show()
            QApplication.processEvents()
            # Build and Show output, wait for it to be closed
            outputProcess = subprocess.Popen("python -m ui.output " + outputFile + " " + name)
            outputProcess.wait()
            self.buildingOutputLabel.hide()
            QApplication.processEvents()  # Progress GUI events


    # Function to call when extracting all and comparing
    def extractAllAndCompare(self):
        self.customScoreLabel.hide()
        names = ["times of india", "the hindu", "guardian", "new york times", "google news", "cnn",
                 "reddit news", "reddit world news", "telegraph", "bbc"]

        today = str(datetime.date.today())
        directory = "./data/allFiles/" + today
        if not os.path.exists(directory):
            os.makedirs(directory)
        storageFile = directory + "/allValueFiles.txt"

        if not os.path.exists(storageFile):
            e = multiprocessing.Event()  # Passing it since argument is required, nothing to sync
            queue = multiprocessing.Queue()  # To get score file from threaded process

            pool = ThreadPool(4)
            results = pool.starmap_async(extractorRunner.runScrapper, zip(names, repeat(e), repeat(queue)), chunksize=1)
            while not results.ready():
                self.extractingAllLabel.setText(_fromUtf8(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-family:'Lucida Calligraphy';\
                    font-weight:600; color:black;\">\
                     Extracting And Analyzing All Sources: " + str(
                        10 - results._number_left) + "/10<u></u></span></p></body></html>"))
                self.extractingAllLabel.show()
                QApplication.processEvents()

            pool.close()
            pool.join()  # Wait for all threads to return

            outputfiles = ""
            for i in range(10):
                outputfiles += " " + queue.get()

            with open(storageFile, "w") as temp:
                temp.write(outputfiles)

        self.extractingAllLabel.hide()
        QApplication.processEvents()
        # Show comparision graph
        outputProcess = subprocess.Popen("python -m ui.comparingAll " + storageFile)

        with open("./data/done.txt", "w") as file:
            file.write("Done")

        outputProcess.wait()
        QApplication.processEvents()


    # Function to call after entering custom headline
    def start_call(self):
        self.customScoreLabel.hide()
        headline = self.lineEdit.text()  # Get entered text from box
        file = "./data/custom.txt"
        with open(file, "w") as f:
            f.write(headline + "\n")
        # For synchronization with loading screen
        e = multiprocessing.Event()
        queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=extractorRunner.runScrapper, args=(file, e, queue)).start()
        # Show loading
        xPos = MainW.geometry().topLeft().x()
        yPos = MainW.geometry().topLeft().y()
        gif = "./images/loading.gif"
        player = ImagePlayer(gif, (xPos + 846), (yPos + 435))
        player.start_movie(e)

        outputFile = queue.get()

        with open(outputFile, "r") as f:
            f.readline()  # Read 1st line
            # Since score is in second line, read it, ignore ">>" from beginning and "\n" from end
            score = f.readline()[3:-1]

        self.customScoreLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-family:'Lucida Calligraphy';font-weight:600; color:black;\">\
            Analyzed Score: " + score + "<u></u></span></p></body></html>"))
        self.customScoreLabel.show()
        QApplication.processEvents()

########################################################################################################################
############################### Graphics elements creation #############################################################
    def setupUi(self, window):
        self.MainWindow = window
        global MainW
        MainW = window

        window.setObjectName(_fromUtf8("window"))
        window.setFixedSize(846, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Project/Images/icon.ico")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        # Background
        window.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/background-images.jpg);\n"
                                       ""))

        ################################################################################################################
        # Times Of India Button
        self.pushButton = QtGui.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(700, 60, 115, 115))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/TOI.png);\n"
                                                "border:none;"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.selected_extractor)

        # The Hindu Button
        self.pushButton_2 = QtGui.QPushButton(window)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 60, 182, 77))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/thehindu.png);\n"
                                                  "border:none;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.selected_extractor)

        # The Guardian Button
        self.pushButton_3 = QtGui.QPushButton(window)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 80, 199, 35))
        self.pushButton_3.setStyleSheet(_fromUtf8("\n"
                                                  "background-image: url(:/images/Project/Images/the-guardian.png);\n"
                                                  "border:none;"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.selected_extractor)

        # New York times Button
        self.pushButton_4 = QtGui.QPushButton(window)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 180, 152, 74))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/NYT.png);\n"
                                                  "border:none;"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.selected_extractor)

        # Google News Button
        self.pushButton_5 = QtGui.QPushButton(window)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 180, 121, 111))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/Googlenews.png);\n"
                                                  "border:none;"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.selected_extractor)

        # CNN button
        self.pushButton_6 = QtGui.QPushButton(window)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 300, 169, 81))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/cnn-m2.png);\n"
                                                  "border:none;"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.selected_extractor)

        # Reddit Button
        self.pushButton_7 = QtGui.QPushButton(window)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 180, 201, 68))
        self.pushButton_7.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/reddit.png);\n"
                                                  "border:none;"))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.clicked.connect(self.selected_extractor)

        # Reddit World News Button
        self.pushButton_8 = QtGui.QPushButton(window)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 220, 112, 105))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/newsicon.png);\n"
                                                  "border:none;"))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.clicked.connect(self.selected_extractor)

        # The Telegraph Button
        self.pushButton_9 = QtGui.QPushButton(window)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 330, 242, 40))
        self.pushButton_9.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/thetelegraph.png);\n"
                                                  "border:none;"))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_9.clicked.connect(self.selected_extractor)

        # BBC Button
        self.pushButton_10 = QtGui.QPushButton(window)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 50, 121, 91))
        self.pushButton_10.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/bbc.png);\n"
                                                   "border:none;"))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_10.clicked.connect(self.selected_extractor)

        # Horizontal Line in main window
        self.line = QtGui.QFrame(window)
        self.line.setGeometry(QtCore.QRect(0, 419, 851, 3))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(20)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))

        # Extract all and conclude button
        self.extractAllButton = QtGui.QPushButton(window)
        self.extractAllButton.setGeometry(QtCore.QRect(250, 428, 300, 30))
        self.extractAllButton.setStyleSheet(_fromUtf8("color:grey; font-size:14pt; font-weight:600; background:#a8ffe9; \
                                                         font-family:'Lucida Calligraphy';border-style: outset;\
                                                         border-width: 2px;border-radius: 15px;border-color:grey;\
                                                        padding: 4px;"))
        self.extractAllButton.setAutoDefault(True)
        self.extractAllButton.isCheckable()
        self.extractAllButton.setText("Extract All And Compare")
        self.extractAllButton.setObjectName(_fromUtf8("extractAllButton"))
        self.extractAllButton.clicked.connect(self.extractAllAndCompare)

        # Custom Headline Text Input Box
        self.lineEdit = QtGui.QLineEdit(window)
        self.lineEdit.setGeometry(QtCore.QRect(20, 470, 671, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(327686)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        # Run button
        self.pushButton_11 = QtGui.QPushButton(window)
        self.pushButton_11.setGeometry(QtCore.QRect(730, 470, 61, 61))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/Play.png);\n"
                                                   "border:none;"))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_11.clicked.connect(self.start_call)

        # Information labels
        self.customScoreLabel = QtGui.QLabel(window)
        self.customScoreLabel.setGeometry(QtCore.QRect(160, 530, 491, 55))
        self.customScoreLabel.setAutoFillBackground(False)
        self.customScoreLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.customScoreLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.customScoreLabel.setTextFormat(QtCore.Qt.RichText)
        self.customScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.customScoreLabel.setWordWrap(True)
        self.customScoreLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.customScoreLabel.setObjectName(_fromUtf8("customScoreLabel"))
        self.customScoreLabel.hide()

        # Building Output label
        self.buildingOutputLabel = QtGui.QLabel(window)
        self.buildingOutputLabel.setGeometry(QtCore.QRect(160, 530, 491, 55))
        self.buildingOutputLabel.setAutoFillBackground(False)
        self.buildingOutputLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.buildingOutputLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.buildingOutputLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;font-family:'Lucida Calligraphy';\
            font-weight:600; color:black;\">\
             **Building Output Window**<u></u></span></p></body></html>"))
        self.buildingOutputLabel.setTextFormat(QtCore.Qt.RichText)
        self.buildingOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.buildingOutputLabel.setWordWrap(True)
        self.buildingOutputLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.buildingOutputLabel.setObjectName(_fromUtf8("buildingOutputLabel"))
        self.buildingOutputLabel.hide()

        # Extracting All label
        self.extractingAllLabel = QtGui.QLabel(window)
        self.extractingAllLabel.setGeometry(QtCore.QRect(130, 530, 600, 55))
        self.extractingAllLabel.setAutoFillBackground(False)
        self.extractingAllLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.extractingAllLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.extractingAllLabel.setTextFormat(QtCore.Qt.RichText)
        self.extractingAllLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.extractingAllLabel.setWordWrap(True)
        self.extractingAllLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.extractingAllLabel.setObjectName(_fromUtf8("extractingAllLabel"))

        # IP address Label
        self.ipAddressLabel = QtGui.QLabel(window)
        self.ipAddressLabel.setGeometry(QtCore.QRect(180, 0, 491, 55))
        self.ipAddressLabel.setAutoFillBackground(False)
        self.ipAddressLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.ipAddressLabel.setFrameShadow(QtGui.QFrame.Plain)
        ip_address = getIpAddress()
        self.ipAddressLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Lucida Calligraphy';\
            font-weight:500; color:green;\">Live on: " + str(ip_address) + "</span></p></body></html>"))
        self.ipAddressLabel.setTextFormat(QtCore.Qt.RichText)
        self.ipAddressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ipAddressLabel.setWordWrap(True)
        self.ipAddressLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ipAddressLabel.setObjectName(_fromUtf8("ipAddressLabel"))

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "Opinion Mining Of News Headlines", None))
        self.lineEdit.setPlaceholderText(
            _translate("window", "    Choose from above, or enter your headline here", None))
