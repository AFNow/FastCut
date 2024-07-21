# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QSizeGrip
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QIcon

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Fast_Cut_Mainwindow

class Fast_Cut_Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Fast_Cut_Mainwindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # The frameless window option
        self.setAttribute(Qt.WA_TranslucentBackground) # The translucent background option

        self.shadow = QGraphicsDropShadowEffect(self) # The shadow effect and its parameters
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 95, 150, 550))
        self.ui.main_frame.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("resources/icons/FastCut.ico")) # The window icon

        self.setWindowTitle("Fast_Cut") # The window title

        #QSizeGrip(self.ui.grip) # The window size grip

        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.expand_button.clicked.connect(lambda: self.maximize_minimize())
        self.ui.roll_button.clicked.connect(lambda: self.showMinimized())

        self.ui.call_side_frame_button.clicked.connect(lambda: self.left_frame_event())

        self.ui.call_dropdown_frame_button.clicked.connect(lambda: self.dropdown_frame_event())


    def maximize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def move_window(self, e):
        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.dragPos = e.globalPos()
                e.accept()
        self.ui.main_frame_header.mouseMoveEvent = self.move_window


    def left_frame_event(self):
        left_frame_width = self.ui.side_frame.width()
        if left_frame_width == 0:
            left_frame_end_width = 250
            #self.ui.call_side_frame_button.setIcon(#new icon address)
        else:
            left_frame_end_width = 0
            #self.ui.call_side_frame_button.setIcon(#old icon address)


        self.animation = QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(left_frame_width)
        self.animation.setEndValue(left_frame_end_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def dropdown_frame_event(self):
        dropdown_frame_height = self.ui.dropdown_frame.height()
        if dropdown_frame_height == 0:
            dropdown_frame_end_height = 40
            #self.ui.call_side_frame_button.setIcon(#new icon address)
        else:
            dropdown_frame_end_height = 0
            #self.ui.call_side_frame_button.setIcon(#old icon address)


        self.animation = QPropertyAnimation(self.ui.dropdown_frame, b"maximumHeight")
        self.animation.setDuration(300)
        self.animation.setStartValue(dropdown_frame_height)
        self.animation.setEndValue(dropdown_frame_end_height)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def mouse_press_events(self, event):
        self.clickPosition = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Fast_Cut_Mainwindow()
    widget.show()
    sys.exit(app.exec())
