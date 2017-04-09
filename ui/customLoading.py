from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore


class ImagePlayer(QtGui.QDialog):
    def __init__(self, filename, x_axis, y_axis, parent=None):
        super(ImagePlayer, self).__init__(parent, flags=QtCore.Qt.FramelessWindowHint)

        # Load the file into a QMovie
        self.movie = QMovie(filename, QByteArray(), self)

        size = self.movie.scaledSize()
        self.setGeometry(x_axis, y_axis, 120, 120)
        self.setStyleSheet("background:black;")
        self.movie_screen = QLabel()
        # Fir our GIF into the label
        self.movie_screen.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        # Create the layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        # Add the QMovie object to the label
        self.movie.setCacheMode(QMovie.CacheAll)  # Cache/Store all frame of our GIF
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.show()

    def start_movie(self, e):
        self.movie.start()
        while not e.is_set():
            QApplication.instance().processEvents()
        self.close()
