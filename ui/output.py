# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlibwidget import MatplotlibWidget
from pyqtgraph import PlotWidget
import images.outputResources
import numpy as np
import pyqtgraph as pg
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from os import path
from wordcloud import WordCloud
import os

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


def drawWordCloud():
    # Read the whole text.
    text = open(r'..\data\googleNews\2017-03-18\2017-03-18.txt').read()
    # Generate a word cloud image
    wordcloud = WordCloud(width=491,height=301).generate(text)
    wordcloud.to_file("..\data\wc.png")


def makeGraph(graphView):
    pg.setConfigOptions(antialias=True)

    y_axis = []
    with open(r'../data/googleNews/2017-03-18/2017-03-18scores.txt', "r") as f:
        for line in f:
            if line.startswith(">>"):
                num = float(line[3:].rstrip("\n"))
                y_axis.append(num)
    x_axis = list(range(1,len(y_axis) + 1))
    graphView.plot(x_axis, y_axis, pen=(200, 200, 200), symbolBrush=(255, 0, 0), symbolPen='b')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1366, 696)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Project/HeadlineMining Gitlab/images/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-image: url(:/bavkground/images/woodback.jpg);"))

        #Graph
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOption('leftButtonPan', False)
        self.Graph = PlotWidget(Dialog)
        self.Graph.setGeometry(QtCore.QRect(670, 30, 651, 321))
        self.Graph.setObjectName(_fromUtf8("Graph"))
        makeGraph(self.Graph)

        # wordCloud
        self.wordCloud = pic = QtGui.QLabel(Dialog)
        self.wordCloud.setGeometry(QtCore.QRect(60, 40, 491, 301))
        self.wordCloud.setObjectName(_fromUtf8("wordCloud"))
        drawWordCloud()
        self.wordCloud.setPixmap(QtGui.QPixmap("..\data\wc.png"))




        #Calender
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(830, 430, 361, 251))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2017, 1, 2))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2017, 12, 31))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.CalenderLabel = QtGui.QLabel(Dialog)
        self.CalenderLabel.setGeometry(QtCore.QRect(770, 370, 491, 51))
        self.CalenderLabel.setAutoFillBackground(False)
        self.CalenderLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.CalenderLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.CalenderLabel.setText(_fromUtf8("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Select a date from calender below to plot that day\'s graph</span></p></body></html>"))
        self.CalenderLabel.setTextFormat(QtCore.Qt.RichText)
        self.CalenderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CalenderLabel.setWordWrap(True)
        self.CalenderLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.CalenderLabel.setObjectName(_fromUtf8("CalenderLabel"))

        #Headline1
        self.Headline1 = QtGui.QLabel(Dialog)
        self.Headline1.setGeometry(QtCore.QRect(40, 370, 521, 51))
        self.Headline1.setStyleSheet(_fromUtf8(""))
        self.Headline1.setTextFormat(QtCore.Qt.RichText)
        self.Headline1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Headline1.setWordWrap(True)
        self.Headline1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Headline1.setObjectName(_fromUtf8("Headline1"))

        #pushbutton
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(670, 480, 81, 81))
        self.pushButton.setStyleSheet(_fromUtf8("background-image: url(:/labelBackground/images/nextButton.png);\n"
"border:none;"))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #Value1
        self.Value1 = QtGui.QLabel(Dialog)
        self.Value1.setGeometry(QtCore.QRect(580, 370, 71, 51))
        self.Value1.setStyleSheet(_fromUtf8("background:transparent;"))
        self.Value1.setTextFormat(QtCore.Qt.RichText)
        self.Value1.setAlignment(QtCore.Qt.AlignCenter)
        self.Value1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Value1.setObjectName(_fromUtf8("Value1"))





        #Headline2
        self.Headline2 = QtGui.QLabel(Dialog)
        self.Headline2.setGeometry(QtCore.QRect(40, 450, 521, 51))
        self.Headline2.setStyleSheet(_fromUtf8(""))
        self.Headline2.setTextFormat(QtCore.Qt.RichText)
        self.Headline2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Headline2.setWordWrap(True)
        self.Headline2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Headline2.setObjectName(_fromUtf8("Headline2"))
        self.Headline3 = QtGui.QLabel(Dialog)
        self.Headline3.setGeometry(QtCore.QRect(40, 530, 521, 51))
        self.Headline3.setStyleSheet(_fromUtf8(""))
        self.Headline3.setTextFormat(QtCore.Qt.RichText)
        self.Headline3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Headline3.setWordWrap(True)
        self.Headline3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Headline3.setObjectName(_fromUtf8("Headline3"))
        self.Headline4 = QtGui.QLabel(Dialog)
        self.Headline4.setGeometry(QtCore.QRect(40, 610, 521, 51))
        self.Headline4.setStyleSheet(_fromUtf8(""))
        self.Headline4.setTextFormat(QtCore.Qt.RichText)
        self.Headline4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Headline4.setWordWrap(True)
        self.Headline4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Headline4.setObjectName(_fromUtf8("Headline4"))
        self.Value4 = QtGui.QLabel(Dialog)
        self.Value4.setGeometry(QtCore.QRect(580, 610, 71, 51))
        self.Value4.setStyleSheet(_fromUtf8("background:transparent;"))
        self.Value4.setTextFormat(QtCore.Qt.RichText)
        self.Value4.setAlignment(QtCore.Qt.AlignCenter)
        self.Value4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Value4.setObjectName(_fromUtf8("Value4"))
        self.Value3 = QtGui.QLabel(Dialog)
        self.Value3.setGeometry(QtCore.QRect(580, 530, 71, 51))
        self.Value3.setStyleSheet(_fromUtf8("background:transparent;"))
        self.Value3.setTextFormat(QtCore.Qt.RichText)
        self.Value3.setAlignment(QtCore.Qt.AlignCenter)
        self.Value3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Value3.setObjectName(_fromUtf8("Value3"))
        self.Value2 = QtGui.QLabel(Dialog)
        self.Value2.setGeometry(QtCore.QRect(580, 450, 71, 51))
        self.Value2.setStyleSheet(_fromUtf8("background:transparent;"))
        self.Value2.setTextFormat(QtCore.Qt.RichText)
        self.Value2.setAlignment(QtCore.Qt.AlignCenter)
        self.Value2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Value2.setObjectName(_fromUtf8("Value2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Headline1.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; color:#ffffff;\">Headline 1</span></p></body></html>", None))
        self.Value1.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">0.0</span></p></body></html>", None))
        self.Headline2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; color:#ffffff;\">Headline 1</span></p></body></html>", None))
        self.Headline3.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; color:#ffffff;\">Headline 1</span></p></body></html>", None))
        self.Headline4.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; color:#ffffff;\">Headline 1</span></p></body></html>", None))
        self.Value4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">0.0</span></p></body></html>", None))
        self.Value3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">0.0</span></p></body></html>", None))
        self.Value2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">0.0</span></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

