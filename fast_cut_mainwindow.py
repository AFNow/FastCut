# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QApplication, QSizeGrip, QGraphicsDropShadowEffect, QFileDialog, QTextEdit
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PySide6 import QtGui
from PySide6.QtGui import QColor, QIcon, QFileOpenEvent

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Fast_Cut_Mainwindow

# Default path address
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
default_path = BASE_DIR

class Fast_Cut_Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Fast_Cut_Mainwindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # The frameless window option
        self.setAttribute(Qt.WA_TranslucentBackground) # The translucent background option
        self.ui.main_frame_header.mousePressEvent = self.mousePressEvent # Mouse press event for the window dragging
        self.ui.main_frame_header.mouseMoveEvent = self.mouseMoveEvent # Mouse move event for the window dragging


        self.shadow = QGraphicsDropShadowEffect(self) # The shadow effect and its parameters
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 95, 150, 550))
        self.ui.main_frame.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("resources/icons/FastCut.ico")) # The window icon

        self.setWindowTitle("Fast_Cut") # The window title

        #QSizeGrip(self.ui.grip) # The window size grip

        # Mainwindow buttons connectors:
        self.ui.close_button.clicked.connect(lambda: self.close()) 
        self.ui.expand_button.clicked.connect(lambda: self.maximize_minimize())
        self.ui.roll_button.clicked.connect(lambda: self.showMinimized())

        #Side frame and dropdown connectors
        self.ui.call_side_frame_button.clicked.connect(lambda: self.left_frame_event())
        self.ui.call_dropdown_frame_button.clicked.connect(lambda: self.dropdown_frame_event())

        #Connectors to the buttons inside side frame 
        self.ui.set_folder_button.clicked.connect(lambda: self.select_path())

        #Connectors to the buttons inside dropdown frame
        self.ui.download_button.clicked.connect(lambda: self.check_link())


    # Window size button function 
    def maximize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    # The side frame event 
    def left_frame_event(self):
        left_frame_width = self.ui.side_frame.width()
        if left_frame_width == 0:
            left_frame_end_width = 250
            icon11 = QIcon() # Assigning the non-default icon's state
            icon11.addFile(u":/sidemenu_caller/resources/icons/sidemenu1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.call_side_frame_button.setIcon(icon11)
        else:
            left_frame_end_width = 0
            icon5 = QIcon() # Assigning the default icon's state back
            icon5.addFile(u":/sidemenu_caller/resources/icons/sidemenu2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.call_side_frame_button.setIcon(icon5)
        #Left frame animation parameters
        self.animation = QPropertyAnimation(self.ui.side_frame, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(left_frame_width)
        self.animation.setEndValue(left_frame_end_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
   
    # Function to select the default path
    def select_path(self):
        global default_path
        dialog = QFileDialog()
        default_path = dialog.getExistingDirectory(None, "Select Folder")
        return default_path


    # Events for the mouse click and mouse move
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.clickPosition)
            event.accept()


    # Dropdown frame event
    def dropdown_frame_event(self):
        dropdown_frame_height = self.ui.dropdown_frame.height()
        if dropdown_frame_height == 0:
            dropdown_frame_end_height = 40
            icon12 = QIcon() # Assigning the non-default icon's state
            icon12.addFile(u":/dropdown_menu/resources/icons/dropdown1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.call_dropdown_frame_button.setIcon(icon12)
        else:
            dropdown_frame_end_height = 0
            icon6 = QIcon() # Assigning the non-default icon's state
            icon6.addFile(u":/dropdown_menu/resources/icons/dropdown2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.ui.call_dropdown_frame_button.setIcon(icon6)
        #Dropdown frame animation parameters
        self.animation = QPropertyAnimation(self.ui.dropdown_frame, b"maximumHeight")
        self.animation.setDuration(300)
        self.animation.setStartValue(dropdown_frame_height)
        self.animation.setEndValue(dropdown_frame_end_height)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    # Dropdown menu functions
    def check_link(self):
        link_text = self.ui.link_line_edit.text()
        print(link_text)
        pass

    # Link checking function for call a video title
#def link_check():
#    link = link_entry.get()
#    if link != "":
#        try:
#            yt = pytube.YouTube(link, on_progress_callback = None)
#            video_title = yt.title
#            video_title_label.configure(text = video_title)
#        except pytube.exceptions.RegexMatchError:
#            video_title_label.configure(text = "Wrog link")
# Threading for link checking
#def link_check_thread(event):
#    thread = Thread(target = link_check, daemon = True)
#    thread.start()
#    return thread


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Fast_Cut_Mainwindow()
    widget.show()
    sys.exit(app.exec())
