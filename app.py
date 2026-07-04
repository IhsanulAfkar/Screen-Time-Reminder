import sys
import cv2
from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QMessageBox
)

from camera.thread import CameraThread
from config import ScreenTimeManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.long_screen_popup_shown = False
        self.setWindowTitle("Eye Break Reminder")
        self.resize(900, 700)

        # Initialize screen time manager
        self.screen_time_manager = ScreenTimeManager()
        self.screen_time_manager.start_session()

        # Create UI elements
        self.cameraLabel = QLabel()
        self.cameraLabel.setAlignment(Qt.AlignCenter)
        
        # Add a label to show screen time
        self.timeLabel = QLabel()
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size: 18px; font-weight: bold; color: blue;")
        
        # Add a label for warnings
        self.warningLabel = QLabel()
        self.warningLabel.setAlignment(Qt.AlignCenter)
        self.warningLabel.setStyleSheet("font-size: 16px; font-weight: bold; color: red;")
        self.warningLabel.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.cameraLabel)
        layout.addWidget(self.warningLabel)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.cameraThread = CameraThread()
        self.cameraThread.frameCaptured.connect(self.updateFrame)
        self.cameraThread.start()

        # Start timer to update screen time display
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateScreenTime)
        self.timer.start(1000)  # Update every second

        # Initial update
        self.updateScreenTime()

    def updateFrame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape

        image = QImage(
            frame.data,
            w,
            h,
            ch * w,
            QImage.Format.Format_RGB888,
        )

        pixmap = QPixmap.fromImage(image)

        self.cameraLabel.setPixmap(
            pixmap.scaled(
                self.cameraLabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
        )

    def updateScreenTime(self):
        """Update the screen time display and check for warnings"""
        # Check if face is detected in camera frame
        face_detected = self.cameraThread.is_face_detected()
        
        if not face_detected:
            # Reset timer when face is not detected
            self.screen_time_manager.reset_session()
            self.long_screen_popup_shown = False
            self.warningLabel.hide()
            print("Face not detected. Timer reset.")
        else:
            # Continue tracking time normally
            pass
        
        # Update screen time display
        current_time = self.screen_time_manager.get_current_time()
        minutes = int(current_time // 60)
        seconds = int(current_time % 60)
        self.timeLabel.setText(f"Screen Time: {minutes}m {seconds}s")
        if current_time >= self.screen_time_manager.get_treshold_timer() and not self.long_screen_popup_shown:
            self.long_screen_popup_shown = True

            QMessageBox.warning(
                self,
                "Screen Time Warning",
                "You looking at screen too long!"
            )
            self.screen_time_manager.reset_session()
            self.long_screen_popup_shown = False
        # Check warning system
        if self.screen_time_manager.check_warning():
            self.warningLabel.setText("Warning: Extended screen time detected!")
            self.warningLabel.show()
            print("Screen time limit exceeded! Take a break.")
        else:
            self.warningLabel.hide()

    def closeEvent(self, event):
        self.screen_time_manager.end_session()
        self.cameraThread.stop()
        self.cameraThread.wait()
        event.accept()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
