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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import rc_resources

class Ui_Fast_Cut_Mainwindow(object):
    def setupUi(self, Fast_Cut_Mainwindow):
        if not Fast_Cut_Mainwindow.objectName():
            Fast_Cut_Mainwindow.setObjectName(u"Fast_Cut_Mainwindow")
        Fast_Cut_Mainwindow.resize(1200, 600)
        self.base_widget = QWidget(Fast_Cut_Mainwindow)
        self.base_widget.setObjectName(u"base_widget")
        self.base_widget.setMinimumSize(QSize(1200, 600))
        self.base_widget.setStyleSheet(u"background-color:rgb(24,24,36);")
        self.horizontalLayout = QHBoxLayout(self.base_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_frame = QFrame(self.base_widget)
        self.side_frame.setObjectName(u"side_frame")
        self.side_frame.setMinimumSize(QSize(0, 0))
        self.side_frame.setMaximumSize(QSize(0, 16777215))
        self.side_frame.setFrameShape(QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.side_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_frame_header = QFrame(self.side_frame)
        self.side_frame_header.setObjectName(u"side_frame_header")
        self.side_frame_header.setMinimumSize(QSize(0, 50))
        self.side_frame_header.setMaximumSize(QSize(16777215, 50))
        self.side_frame_header.setStyleSheet(u"background-color: rgb(0, 4, 31)")
        self.side_frame_header.setFrameShape(QFrame.StyledPanel)
        self.side_frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.side_frame_header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.link_button = QPushButton(self.side_frame_header)
        self.link_button.setObjectName(u"link_button")
        self.link_button.setMinimumSize(QSize(0, 50))
        self.link_button.setMaximumSize(QSize(16777215, 50))
        icon = QIcon()
        icon.addFile(u":/resources/icons/resources/icons/header.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.link_button.setIcon(icon)
        self.link_button.setIconSize(QSize(120, 40))
        self.link_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.link_button)


        self.verticalLayout.addWidget(self.side_frame_header)

        self.side_frame_content = QFrame(self.side_frame)
        self.side_frame_content.setObjectName(u"side_frame_content")
        self.side_frame_content.setStyleSheet(u"background-color: rgb(0, 4, 31)")
        self.side_frame_content.setFrameShape(QFrame.StyledPanel)
        self.side_frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.side_frame_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.scrollArea = QScrollArea(self.side_frame_content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setContextMenuPolicy(Qt.NoContextMenu)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -74, 225, 570))
        self.scrollAreaWidgetContents.setContextMenuPolicy(Qt.NoContextMenu)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.file_frame_1 = QFrame(self.scrollAreaWidgetContents)
        self.file_frame_1.setObjectName(u"file_frame_1")
        self.file_frame_1.setMinimumSize(QSize(210, 135))
        self.file_frame_1.setMaximumSize(QSize(210, 135))
        self.file_frame_1.setStyleSheet(u"border-radius: 16;\n"
"background-color: rgb(100,100,100);")
        self.file_frame_1.setFrameShape(QFrame.StyledPanel)
        self.file_frame_1.setFrameShadow(QFrame.Raised)
        self.name_background_1 = QFrame(self.file_frame_1)
        self.name_background_1.setObjectName(u"name_background_1")
        self.name_background_1.setGeometry(QRect(0, 110, 225, 34))
        self.name_background_1.setMinimumSize(QSize(225, 0))
        self.name_background_1.setMaximumSize(QSize(225, 16777215))
        self.name_background_1.setStyleSheet(u"background-color: rgb(100,100,200);")
        self.name_background_1.setFrameShape(QFrame.StyledPanel)
        self.name_background_1.setFrameShadow(QFrame.Raised)
        self.name_label_1 = QLabel(self.name_background_1)
        self.name_label_1.setObjectName(u"name_label_1")
        self.name_label_1.setGeometry(QRect(0, 5, 225, 16))
        self.name_label_1.setMinimumSize(QSize(225, 0))
        self.name_label_1.setMaximumSize(QSize(225, 16777215))
        self.name_label_1.setLayoutDirection(Qt.LeftToRight)
        self.name_label_1.setStyleSheet(u"color: white;")
        self.name_label_1.setFrameShape(QFrame.NoFrame)
        self.name_label_1.setTextFormat(Qt.PlainText)
        self.name_label_1.setScaledContents(False)
        self.name_label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.file_frame_1)

        self.file_frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.file_frame_2.setObjectName(u"file_frame_2")
        self.file_frame_2.setMinimumSize(QSize(210, 135))
        self.file_frame_2.setMaximumSize(QSize(210, 135))
        self.file_frame_2.setStyleSheet(u"border-radius: 16;\n"
"background-color: rgb(100,100,100);")
        self.file_frame_2.setFrameShape(QFrame.StyledPanel)
        self.file_frame_2.setFrameShadow(QFrame.Raised)
        self.name_background_2 = QFrame(self.file_frame_2)
        self.name_background_2.setObjectName(u"name_background_2")
        self.name_background_2.setGeometry(QRect(0, 110, 225, 34))
        self.name_background_2.setMinimumSize(QSize(225, 0))
        self.name_background_2.setMaximumSize(QSize(225, 16777215))
        self.name_background_2.setStyleSheet(u"background-color: rgb(100,100,200);")
        self.name_background_2.setFrameShape(QFrame.StyledPanel)
        self.name_background_2.setFrameShadow(QFrame.Raised)
        self.name_label_2 = QLabel(self.name_background_2)
        self.name_label_2.setObjectName(u"name_label_2")
        self.name_label_2.setGeometry(QRect(0, 5, 225, 16))
        self.name_label_2.setMinimumSize(QSize(225, 0))
        self.name_label_2.setMaximumSize(QSize(225, 16777215))
        self.name_label_2.setLayoutDirection(Qt.LeftToRight)
        self.name_label_2.setStyleSheet(u"color: white;")
        self.name_label_2.setFrameShape(QFrame.NoFrame)
        self.name_label_2.setTextFormat(Qt.PlainText)
        self.name_label_2.setScaledContents(False)
        self.name_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.file_frame_2)

        self.file_frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.file_frame_3.setObjectName(u"file_frame_3")
        self.file_frame_3.setMinimumSize(QSize(210, 135))
        self.file_frame_3.setMaximumSize(QSize(210, 135))
        self.file_frame_3.setStyleSheet(u"border-radius: 16;\n"
"background-color: rgb(100,100,100);")
        self.file_frame_3.setFrameShape(QFrame.StyledPanel)
        self.file_frame_3.setFrameShadow(QFrame.Raised)
        self.name_background_3 = QFrame(self.file_frame_3)
        self.name_background_3.setObjectName(u"name_background_3")
        self.name_background_3.setGeometry(QRect(0, 110, 225, 34))
        self.name_background_3.setMinimumSize(QSize(225, 0))
        self.name_background_3.setMaximumSize(QSize(225, 16777215))
        self.name_background_3.setStyleSheet(u"background-color: rgb(100,100,200);")
        self.name_background_3.setFrameShape(QFrame.StyledPanel)
        self.name_background_3.setFrameShadow(QFrame.Raised)
        self.name_label_3 = QLabel(self.name_background_3)
        self.name_label_3.setObjectName(u"name_label_3")
        self.name_label_3.setGeometry(QRect(0, 5, 225, 16))
        self.name_label_3.setMinimumSize(QSize(225, 0))
        self.name_label_3.setMaximumSize(QSize(225, 16777215))
        self.name_label_3.setLayoutDirection(Qt.LeftToRight)
        self.name_label_3.setStyleSheet(u"color: white;")
        self.name_label_3.setFrameShape(QFrame.NoFrame)
        self.name_label_3.setTextFormat(Qt.PlainText)
        self.name_label_3.setScaledContents(False)
        self.name_label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.file_frame_3)

        self.file_frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.file_frame_4.setObjectName(u"file_frame_4")
        self.file_frame_4.setMinimumSize(QSize(210, 135))
        self.file_frame_4.setMaximumSize(QSize(210, 135))
        self.file_frame_4.setStyleSheet(u"border-radius: 16;\n"
"background-color: rgb(100,100,100);")
        self.file_frame_4.setFrameShape(QFrame.StyledPanel)
        self.file_frame_4.setFrameShadow(QFrame.Raised)
        self.name_background_4 = QFrame(self.file_frame_4)
        self.name_background_4.setObjectName(u"name_background_4")
        self.name_background_4.setGeometry(QRect(0, 110, 225, 34))
        self.name_background_4.setMinimumSize(QSize(225, 0))
        self.name_background_4.setMaximumSize(QSize(225, 16777215))
        self.name_background_4.setStyleSheet(u"background-color: rgb(100,100,200);")
        self.name_background_4.setFrameShape(QFrame.StyledPanel)
        self.name_background_4.setFrameShadow(QFrame.Raised)
        self.name_label_4 = QLabel(self.name_background_4)
        self.name_label_4.setObjectName(u"name_label_4")
        self.name_label_4.setGeometry(QRect(0, 5, 225, 16))
        self.name_label_4.setMinimumSize(QSize(225, 0))
        self.name_label_4.setMaximumSize(QSize(225, 16777215))
        self.name_label_4.setLayoutDirection(Qt.LeftToRight)
        self.name_label_4.setStyleSheet(u"color: white;")
        self.name_label_4.setFrameShape(QFrame.NoFrame)
        self.name_label_4.setTextFormat(Qt.PlainText)
        self.name_label_4.setScaledContents(False)
        self.name_label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.file_frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.side_frame_content)

        self.side_frame_bottom = QFrame(self.side_frame)
        self.side_frame_bottom.setObjectName(u"side_frame_bottom")
        self.side_frame_bottom.setMinimumSize(QSize(0, 50))
        self.side_frame_bottom.setMaximumSize(QSize(16777215, 50))
        self.side_frame_bottom.setStyleSheet(u"background-color: rgb(0, 4, 31)")
        self.side_frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.side_frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.side_frame_bottom)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.file_operations_frame = QFrame(self.side_frame_bottom)
        self.file_operations_frame.setObjectName(u"file_operations_frame")
        self.file_operations_frame.setFrameShape(QFrame.StyledPanel)
        self.file_operations_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.file_operations_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.open_file_button = QPushButton(self.file_operations_frame)
        self.open_file_button.setObjectName(u"open_file_button")
        self.open_file_button.setMinimumSize(QSize(30, 30))
        self.open_file_button.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/resources/icons/resources/icons/open_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_file_button.setIcon(icon1)
        self.open_file_button.setIconSize(QSize(30, 30))
        self.open_file_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.open_file_button)

        self.save_file_button = QPushButton(self.file_operations_frame)
        self.save_file_button.setObjectName(u"save_file_button")
        self.save_file_button.setMinimumSize(QSize(30, 30))
        self.save_file_button.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/resources/icons/resources/icons/save_file.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.save_file_button.setIcon(icon2)
        self.save_file_button.setIconSize(QSize(30, 30))
        self.save_file_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.save_file_button)


        self.horizontalLayout_4.addWidget(self.file_operations_frame)

        self.folder_operations_frame = QFrame(self.side_frame_bottom)
        self.folder_operations_frame.setObjectName(u"folder_operations_frame")
        self.folder_operations_frame.setFrameShape(QFrame.StyledPanel)
        self.folder_operations_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.folder_operations_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.open_folder_button = QPushButton(self.folder_operations_frame)
        self.open_folder_button.setObjectName(u"open_folder_button")
        self.open_folder_button.setMinimumSize(QSize(30, 30))
        self.open_folder_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/resources/icons/resources/icons/open_folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.open_folder_button.setIcon(icon3)
        self.open_folder_button.setIconSize(QSize(30, 30))
        self.open_folder_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.open_folder_button)

        self.set_folder_button = QPushButton(self.folder_operations_frame)
        self.set_folder_button.setObjectName(u"set_folder_button")
        self.set_folder_button.setMinimumSize(QSize(30, 30))
        self.set_folder_button.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/resources/icons/resources/icons/select_folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.set_folder_button.setIcon(icon4)
        self.set_folder_button.setIconSize(QSize(30, 30))
        self.set_folder_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.set_folder_button)


        self.horizontalLayout_4.addWidget(self.folder_operations_frame)


        self.verticalLayout.addWidget(self.side_frame_bottom)


        self.horizontalLayout.addWidget(self.side_frame)

        self.main_frame = QFrame(self.base_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color:rgb(24,24,36);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_frame_header = QFrame(self.main_frame)
        self.main_frame_header.setObjectName(u"main_frame_header")
        self.main_frame_header.setMinimumSize(QSize(0, 50))
        self.main_frame_header.setMaximumSize(QSize(16777215, 50))
        self.main_frame_header.setStyleSheet(u"background-color: rgb(0, 4, 31)")
        self.main_frame_header.setFrameShape(QFrame.StyledPanel)
        self.main_frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_frame_header)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.main_frame_header_side_call = QFrame(self.main_frame_header)
        self.main_frame_header_side_call.setObjectName(u"main_frame_header_side_call")
        self.main_frame_header_side_call.setMinimumSize(QSize(50, 0))
        self.main_frame_header_side_call.setMaximumSize(QSize(50, 16777215))
        self.main_frame_header_side_call.setFrameShape(QFrame.StyledPanel)
        self.main_frame_header_side_call.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.main_frame_header_side_call)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.call_side_frame_button = QPushButton(self.main_frame_header_side_call)
        self.call_side_frame_button.setObjectName(u"call_side_frame_button")
        self.call_side_frame_button.setMinimumSize(QSize(30, 30))
        self.call_side_frame_button.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/resources/icons/resources/icons/side_menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.call_side_frame_button.setIcon(icon5)
        self.call_side_frame_button.setIconSize(QSize(30, 30))
        self.call_side_frame_button.setFlat(True)

        self.horizontalLayout_9.addWidget(self.call_side_frame_button)


        self.horizontalLayout_7.addWidget(self.main_frame_header_side_call)

        self.search_frame = QFrame(self.main_frame_header)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.link_line_edit = QLineEdit(self.search_frame)
        self.link_line_edit.setObjectName(u"link_line_edit")
        self.link_line_edit.setStyleSheet(u"border-radius:5;\n"
"background-color:rgb(0,0,0);\n"
"border: 2px solid white;")

        self.horizontalLayout_10.addWidget(self.link_line_edit)

        self.downloa_button = QPushButton(self.search_frame)
        self.downloa_button.setObjectName(u"downloa_button")
        self.downloa_button.setMinimumSize(QSize(30, 30))
        self.downloa_button.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/resources/icons/resources/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloa_button.setIcon(icon6)
        self.downloa_button.setIconSize(QSize(30, 30))
        self.downloa_button.setFlat(True)

        self.horizontalLayout_10.addWidget(self.downloa_button)


        self.horizontalLayout_7.addWidget(self.search_frame)

        self.window_operators_frame = QFrame(self.main_frame_header)
        self.window_operators_frame.setObjectName(u"window_operators_frame")
        self.window_operators_frame.setMinimumSize(QSize(150, 0))
        self.window_operators_frame.setMaximumSize(QSize(150, 16777215))
        self.window_operators_frame.setFrameShape(QFrame.StyledPanel)
        self.window_operators_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.window_operators_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.roll_button = QPushButton(self.window_operators_frame)
        self.roll_button.setObjectName(u"roll_button")
        self.roll_button.setMinimumSize(QSize(30, 30))
        self.roll_button.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/resources/icons/resources/icons/roll_down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.roll_button.setIcon(icon7)
        self.roll_button.setIconSize(QSize(25, 30))
        self.roll_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.roll_button)

        self.expand_button = QPushButton(self.window_operators_frame)
        self.expand_button.setObjectName(u"expand_button")
        self.expand_button.setMinimumSize(QSize(30, 30))
        self.expand_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/resources/icons/resources/icons/expand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expand_button.setIcon(icon8)
        self.expand_button.setIconSize(QSize(25, 30))
        self.expand_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.expand_button)

        self.close_button = QPushButton(self.window_operators_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(30, 30))
        self.close_button.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/resources/icons/resources/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon9)
        self.close_button.setIconSize(QSize(25, 30))
        self.close_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.close_button)


        self.horizontalLayout_7.addWidget(self.window_operators_frame)


        self.verticalLayout_3.addWidget(self.main_frame_header)

        self.main_frame_content = QFrame(self.main_frame)
        self.main_frame_content.setObjectName(u"main_frame_content")
        self.main_frame_content.setFrameShape(QFrame.StyledPanel)
        self.main_frame_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.main_frame_content)

        self.main_frame_bottom = QFrame(self.main_frame)
        self.main_frame_bottom.setObjectName(u"main_frame_bottom")
        self.main_frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.main_frame_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.main_frame_bottom)

        self.main_frame_content.raise_()
        self.main_frame_bottom.raise_()
        self.main_frame_header.raise_()

        self.horizontalLayout.addWidget(self.main_frame)

        Fast_Cut_Mainwindow.setCentralWidget(self.base_widget)

        self.retranslateUi(Fast_Cut_Mainwindow)

        QMetaObject.connectSlotsByName(Fast_Cut_Mainwindow)
    # setupUi

    def retranslateUi(self, Fast_Cut_Mainwindow):
        Fast_Cut_Mainwindow.setWindowTitle(QCoreApplication.translate("Fast_Cut_Mainwindow", u"Fast_Cut_Mainwindow", None))
        self.link_button.setText("")
        self.name_label_1.setText(QCoreApplication.translate("Fast_Cut_Mainwindow", u"file_name", None))
        self.name_label_2.setText(QCoreApplication.translate("Fast_Cut_Mainwindow", u"file_name", None))
        self.name_label_3.setText(QCoreApplication.translate("Fast_Cut_Mainwindow", u"file_name", None))
        self.name_label_4.setText(QCoreApplication.translate("Fast_Cut_Mainwindow", u"file_name", None))
        self.open_file_button.setText("")
        self.save_file_button.setText("")
        self.open_folder_button.setText("")
        self.set_folder_button.setText("")
        self.call_side_frame_button.setText("")
        self.downloa_button.setText("")
        self.roll_button.setText("")
        self.expand_button.setText("")
        self.close_button.setText("")
    # retranslateUi

