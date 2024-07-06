import sys # System info for app object

import cv2 # OpenCV Library for images and video processing

import pytube # YouTube Downloader

from threading import Thread # Threading

from PyQt5.QtWidgets import QStyleFactory # The styles for the window
from PyQt5.QtCore import Qt, QTimer # The core non-GUI functions fo PyQt and functions for timer
from PyQt5.QtGui import QImage, QPixmap # The functions for displaying images and video 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget # The main GUI subclasses for PyQt

import os # The directory system
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')
font_path = os.path.join(BASE_DIR, 'resources/font.ttf')
folder_icon_path = os.path.join(BASE_DIR, 'resources/folder_icon.png')
download_icon_path = os.path.join(BASE_DIR, 'resources/download_icon.png')
save_path = BASE_DIR

class MainWindow(QMainWindow):
    def __init__(self): # The main window parameters
        super(MainWindow, self).__init__()
        self.setWindowTitle('FastCut')
        self.setGeometry(100, 100, 1500, 900) # Set the position and the size of the window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('FastCut')
    app.setStyle('Windows') # Styles: ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'windowsvista' 'Fusion'], check available styles: print(QStyleFactory.keys())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())