import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.video_label = QLabel()
        self.layout.addWidget(self.video_label)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)
        self.layout.addWidget(self.play_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.video_path = "Downloads/30946_84357cc6034102ff.mp4"
        self.cap = cv2.VideoCapture(self.video_path)

    def play_video(self):
        if not self.timer.isActive():
            self.timer.start(33)  # ~30 fps
            self.play_button.setText("Pause")
        else:
            self.timer.stop()
            self.play_button.setText("Play")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            self.video_label.setPixmap(pixmap.scaled(self.video_label.size(), Qt.KeepAspectRatio))
        else:
            self.timer.stop()
            self.play_button.setText("Play")
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def closeEvent(self, event):
        self.cap.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Breeze')

    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())