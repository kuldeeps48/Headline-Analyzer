# -*- coding: utf-8 -*-

import sys
from datetime import date
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
from pyqtgraph import PlotWidget
import numpy as np

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

displayingfile = []  # File on which output is being calcuated


def makeGraph(graphView):
    global displayingfile
    pg.setConfigOptions(antialias=True)

    prev = 2
    for file in displayingfile:
        y_axis_pos = []
        y_axis_neg = []
        y_axis_zero = []
        with open(file, "r") as f:
            for line in f:
                if line.startswith(">>"):
                    num = float(line[3:].rstrip("\n"))

                    if num > 0:
                        y_axis_pos.append(num)
                    if num < 0:
                        y_axis_neg.append(num)
                    if num == 0:
                        y_axis_zero.append(1)
        pos_x = [prev]
        neg_x = [prev + 0.5]
        neu_x = [prev + 1]
        pos_y = [sum(y_axis_pos)]
        neg_y = [abs(sum(y_axis_neg))]
        neu_y = [sum(y_axis_zero)]
        pos = pg.BarGraphItem(x=np.array(pos_x), height=np.array(pos_y), width=0.5, brush=(0, 198, 53))
        neg = pg.BarGraphItem(x=np.array(neg_x), height=np.array(neg_y), width=0.5, brush=(255, 94, 94))
        neutral = pg.BarGraphItem(x=np.array(neu_x), height=np.array(neu_y), width=0.5, brush=(232, 255, 248))
        graphView.addItem(pos)
        graphView.addItem(neg)
        graphView.addItem(neutral)
        prev += 2

    graphView.hideAxis('bottom')
    graphView.plot()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(900, 350)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        Dialog.setWindowTitle("Comparision Of All News Sources")
        Dialog.setStyleSheet("background:#e2094a")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Project/HeadlineMining Gitlab/images/icon.ico")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)

        # Graph
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOption('leftButtonPan', False)
        self.Graph = PlotWidget(Dialog)
        self.Graph.setGeometry(QtCore.QRect(0, 0, 900, 330))
        self.Graph.setObjectName(_fromUtf8("Graph"))
        makeGraph(self.Graph)

        # Labels
        self.sourceLabel = QtGui.QLabel(Dialog)
        self.sourceLabel.setGeometry(QtCore.QRect(-10, 328, 100, 22))
        self.sourceLabel.setAutoFillBackground(False)
        self.sourceLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.sourceLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.sourceLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Sources:</span></p></body></html>"))
        self.sourceLabel.setTextFormat(QtCore.Qt.RichText)
        self.sourceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceLabel.setWordWrap(True)
        self.sourceLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sourceLabel.setObjectName(_fromUtf8("sourceLabel"))

        self.TOILabel = QtGui.QLabel(Dialog)
        self.TOILabel.setGeometry(QtCore.QRect(765, 328, 100, 22))
        self.TOILabel.setAutoFillBackground(False)
        self.TOILabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.TOILabel.setFrameShadow(QtGui.QFrame.Plain)
        self.TOILabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            TOI</span></p></body></html>"))
        self.TOILabel.setTextFormat(QtCore.Qt.RichText)
        self.TOILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TOILabel.setWordWrap(True)
        self.TOILabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.TOILabel.setObjectName(_fromUtf8("TOILabel"))

        self.TheHinduLabel = QtGui.QLabel(Dialog)
        self.TheHinduLabel.setGeometry(QtCore.QRect(688, 328, 100, 22))
        self.TheHinduLabel.setAutoFillBackground(False)
        self.TheHinduLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.TheHinduLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.TheHinduLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Hindu</span></p></body></html>"))
        self.TheHinduLabel.setTextFormat(QtCore.Qt.RichText)
        self.TheHinduLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TheHinduLabel.setWordWrap(True)
        self.TheHinduLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.TheHinduLabel.setObjectName(_fromUtf8("TheHinduLabel"))

        self.guardianLabel = QtGui.QLabel(Dialog)
        self.guardianLabel.setGeometry(QtCore.QRect(612, 328, 100, 22))
        self.guardianLabel.setAutoFillBackground(False)
        self.guardianLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.guardianLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.guardianLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Guardian</span></p></body></html>"))
        self.guardianLabel.setTextFormat(QtCore.Qt.RichText)
        self.guardianLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.guardianLabel.setWordWrap(True)
        self.guardianLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.guardianLabel.setObjectName(_fromUtf8("guardianLabel"))

        self.nytLabel = QtGui.QLabel(Dialog)
        self.nytLabel.setGeometry(QtCore.QRect(305, 328, 100, 22))
        self.nytLabel.setAutoFillBackground(False)
        self.nytLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.nytLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.nytLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            NYT</span></p></body></html>"))
        self.nytLabel.setTextFormat(QtCore.Qt.RichText)
        self.nytLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nytLabel.setWordWrap(True)
        self.nytLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.nytLabel.setObjectName(_fromUtf8("nytLabel"))

        self.googleLabel = QtGui.QLabel(Dialog)
        self.googleLabel.setGeometry(QtCore.QRect(227, 328, 100, 22))
        self.googleLabel.setAutoFillBackground(False)
        self.googleLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.googleLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.googleLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Google</span></p></body></html>"))
        self.googleLabel.setTextFormat(QtCore.Qt.RichText)
        self.googleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.googleLabel.setWordWrap(True)
        self.googleLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.googleLabel.setObjectName(_fromUtf8("googleLabel"))

        self.cnnLabel = QtGui.QLabel(Dialog)
        self.cnnLabel.setGeometry(QtCore.QRect(150, 328, 100, 22))
        self.cnnLabel.setAutoFillBackground(False)
        self.cnnLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.cnnLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.cnnLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            CNN</span></p></body></html>"))
        self.cnnLabel.setTextFormat(QtCore.Qt.RichText)
        self.cnnLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cnnLabel.setWordWrap(True)
        self.cnnLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.cnnLabel.setObjectName(_fromUtf8("cnnLabel"))

        self.redditLabel = QtGui.QLabel(Dialog)
        self.redditLabel.setGeometry(QtCore.QRect(377, 328, 100, 22))
        self.redditLabel.setAutoFillBackground(False)
        self.redditLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.redditLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.redditLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Reddit</span></p></body></html>"))
        self.redditLabel.setTextFormat(QtCore.Qt.RichText)
        self.redditLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.redditLabel.setWordWrap(True)
        self.redditLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.redditLabel.setObjectName(_fromUtf8("redditLabel"))

        self.worldnewsLabel = QtGui.QLabel(Dialog)
        self.worldnewsLabel.setGeometry(QtCore.QRect(455, 328, 100, 22))
        self.worldnewsLabel.setAutoFillBackground(False)
        self.worldnewsLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.worldnewsLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.worldnewsLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            WorldNews</span></p></body></html>"))
        self.worldnewsLabel.setTextFormat(QtCore.Qt.RichText)
        self.worldnewsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.worldnewsLabel.setWordWrap(True)
        self.worldnewsLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.worldnewsLabel.setObjectName(_fromUtf8("worldnewsLabel"))

        self.telegraphLabel = QtGui.QLabel(Dialog)
        self.telegraphLabel.setGeometry(QtCore.QRect(535, 328, 100, 22))
        self.telegraphLabel.setAutoFillBackground(False)
        self.telegraphLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.telegraphLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.telegraphLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            Telegraph</span></p></body></html>"))
        self.telegraphLabel.setTextFormat(QtCore.Qt.RichText)
        self.telegraphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.telegraphLabel.setWordWrap(True)
        self.telegraphLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.telegraphLabel.setObjectName(_fromUtf8("telegraphLabel"))

        self.bbcLabel = QtGui.QLabel(Dialog)
        self.bbcLabel.setGeometry(QtCore.QRect(72, 328, 100, 22))
        self.bbcLabel.setAutoFillBackground(False)
        self.bbcLabel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.bbcLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.bbcLabel.setText(_fromUtf8(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;font-family:'Times New Roman';font-weight:600; color:white;\">\
            BBC</span></p></body></html>"))
        self.bbcLabel.setTextFormat(QtCore.Qt.RichText)
        self.bbcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bbcLabel.setWordWrap(True)
        self.bbcLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.bbcLabel.setObjectName(_fromUtf8("bbcLabel"))


def showOutput():
    global displayingfile
    temp = sys.argv[1].split()  # Take scores file as command line argument #testing
    with open(sys.argv[1], "r") as f:
        displayingfile = f.readlines()[0].split()
    displayingfile = sorted(displayingfile)
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.processEvents()
    sys.exit(app.exec_())


if __name__ == "__main__":
    showOutput()
