# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QScrollBar, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(942, 655)
        font = QFont()
        font.setFamilies([u"Roboto"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(25, 25))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.full_window_widget = QWidget(MainWindow)
        self.full_window_widget.setObjectName(u"full_window_widget")
        self.horizontalLayout = QHBoxLayout(self.full_window_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_frame = QFrame(self.full_window_widget)
        self.side_frame.setObjectName(u"side_frame")
        self.side_frame.setMaximumSize(QSize(250, 16777215))
        self.side_frame.setFrameShape(QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_frame_header = QFrame(self.side_frame)
        self.side_frame_header.setObjectName(u"side_frame_header")
        self.side_frame_header.setMaximumSize(QSize(16777215, 50))
        self.side_frame_header.setFrameShape(QFrame.StyledPanel)
        self.side_frame_header.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.side_frame_header)

        self.side_frame_content = QFrame(self.side_frame)
        self.side_frame_content.setObjectName(u"side_frame_content")
        self.side_frame_content.setFrameShape(QFrame.StyledPanel)
        self.side_frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.side_frame_content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar = QScrollBar(self.side_frame_content)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.verticalScrollBar)

        self.frame = QFrame(self.side_frame_content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.content_frame1 = QFrame(self.frame)
        self.content_frame1.setObjectName(u"content_frame1")
        self.content_frame1.setFrameShape(QFrame.StyledPanel)
        self.content_frame1.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.content_frame1)

        self.content_frame2 = QFrame(self.frame)
        self.content_frame2.setObjectName(u"content_frame2")
        self.content_frame2.setFrameShape(QFrame.StyledPanel)
        self.content_frame2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.content_frame2)

        self.content_frame3 = QFrame(self.frame)
        self.content_frame3.setObjectName(u"content_frame3")
        self.content_frame3.setFrameShape(QFrame.StyledPanel)
        self.content_frame3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.content_frame3)

        self.content_frame4 = QFrame(self.frame)
        self.content_frame4.setObjectName(u"content_frame4")
        self.content_frame4.setFrameShape(QFrame.StyledPanel)
        self.content_frame4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.content_frame4)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.side_frame_content)

        self.side_frame_bottom = QFrame(self.side_frame)
        self.side_frame_bottom.setObjectName(u"side_frame_bottom")
        self.side_frame_bottom.setMaximumSize(QSize(16777215, 50))
        self.side_frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.side_frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.side_frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.file_operations = QFrame(self.side_frame_bottom)
        self.file_operations.setObjectName(u"file_operations")
        self.file_operations.setFrameShape(QFrame.StyledPanel)
        self.file_operations.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.file_operations)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.open_file_button = QPushButton(self.file_operations)
        self.open_file_button.setObjectName(u"open_file_button")
        self.open_file_button.setEnabled(True)
        self.open_file_button.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"../resources/Icons/open_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_file_button.setIcon(icon)
        self.open_file_button.setIconSize(QSize(25, 25))
        self.open_file_button.setAutoDefault(False)
        self.open_file_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.open_file_button)

        self.save_file_button = QPushButton(self.file_operations)
        self.save_file_button.setObjectName(u"save_file_button")

        self.horizontalLayout_4.addWidget(self.save_file_button)


        self.horizontalLayout_2.addWidget(self.file_operations)

        self.folder_operations = QFrame(self.side_frame_bottom)
        self.folder_operations.setObjectName(u"folder_operations")
        self.folder_operations.setFrameShape(QFrame.StyledPanel)
        self.folder_operations.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.folder_operations)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.open_folder_button = QPushButton(self.folder_operations)
        self.open_folder_button.setObjectName(u"open_folder_button")

        self.horizontalLayout_5.addWidget(self.open_folder_button)

        self.select_folder_button = QPushButton(self.folder_operations)
        self.select_folder_button.setObjectName(u"select_folder_button")

        self.horizontalLayout_5.addWidget(self.select_folder_button)


        self.horizontalLayout_2.addWidget(self.folder_operations)


        self.verticalLayout.addWidget(self.side_frame_bottom)


        self.horizontalLayout.addWidget(self.side_frame)

        self.frame_2 = QFrame(self.full_window_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.full_window_widget)

        self.retranslateUi(MainWindow)

        self.open_file_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_file_button.setText("")
        self.save_file_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.open_folder_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.select_folder_button.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

