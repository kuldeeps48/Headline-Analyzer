# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
sys.path.insert(0, './images')
import mainuiImages

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

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(846, 582)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/Project/Images/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/background-images.jpg);\n"
""))
        self.pushButton = QtGui.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(700, 60, 115, 115))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/TOI.png);\n"
"border:none;"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(window)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 60, 182, 77))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/thehindu.png);\n"
"border:none;"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(window)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 80, 199, 35))
        self.pushButton_3.setStyleSheet(_fromUtf8("\n"
"background-image: url(:/images/Project/Images/the-guardian.png);\n"
"border:none;"))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(window)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 180, 152, 74))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/NYT.png);\n"
"border:none;"))
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(window)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 180, 121, 111))
        self.pushButton_5.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/Googlenews.png);\n"
"border:none;"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(window)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 300, 169, 81))
        self.pushButton_6.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/cnn-m2.png);\n"
"border:none;"))
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(window)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 180, 201, 68))
        self.pushButton_7.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/reddit.png);\n"
"border:none;"))
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(window)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 220, 112, 105))
        self.pushButton_8.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/newsicon.png);\n"
"border:none;"))
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(window)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 330, 242, 40))
        self.pushButton_9.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/thetelegraph.png);\n"
"border:none;"))
        self.pushButton_9.setText(_fromUtf8(""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(window)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 50, 121, 91))
        self.pushButton_10.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/bbc.png);\n"
"border:none;"))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
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
        self.pushButton_11 = QtGui.QPushButton(window)
        self.pushButton_11.setGeometry(QtCore.QRect(730, 470, 61, 61))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(_fromUtf8("background-image: url(:/images/Project/Images/Play.png);\n"
"border:none;"))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(_translate("window", "Opinion Mining Of News Headlines", None))
        self.lineEdit.setPlaceholderText(_translate("window", "    Choose from above, or enter your headline here", None))



def startUI():
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

