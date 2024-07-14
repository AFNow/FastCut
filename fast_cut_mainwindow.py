# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

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
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Fast_Cut_Mainwindow()
    widget.show()
    sys.exit(app.exec())
