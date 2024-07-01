import sys # System info for app object

import cv2 # OpenCV Library for images and video processing

from PyQt5.QtCore import Qt, QTimer # The core non-GUI functions fo PyQt and functions for timer
from PyQt5.QtGui import QImage, QPixmap # The functions for displaying images and video 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget # The main GUI subclasses for PyQt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())