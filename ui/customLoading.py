from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore
import sys


class ImagePlayer(QWidget):
    def __init__(self, filename, x_axis, y_axis, parent=None):
        QWidget.__init__(self, parent, flags=QtCore.Qt.FramelessWindowHint)

        # Load the file into a QMovie
        self.movie = QMovie(filename, QByteArray(), self)

        size = self.movie.scaledSize()
        self.setGeometry(x_axis, y_axis, 120, 120)
        self.setStyleSheet("background:black;")
        self.movie_screen = QLabel()
        # Make label fit the gif
        self.movie_screen.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        # Create the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    gif = "./images/loading.gif"
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    player = ImagePlayer(gif, (x + 846), (y + 435))
    player.show()
    sys.exit(app.exec_())
