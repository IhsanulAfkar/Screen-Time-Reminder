import cv2

from PySide6.QtCore import QThread, Signal

from camera.webcam import Webcam
from camera.face_detector import FaceDetector

class CameraThread(QThread):
    frameCaptured = Signal(object)

    def __init__(self):
        super().__init__()

        self.running = True
        self.webcam = Webcam()
        self.face_detector = FaceDetector()
        
        # Timer control for screen time tracking
        self.face_detected = True  # Start with face detected
        self.last_face_detection_time = None
        
    def run(self):
        while self.running:
            success, frame = self.webcam.read()

            if not success:
                continue

            frame = cv2.flip(frame, 1)

            # Check for face detection
            self.face_detected = self.face_detector.is_face_detected(frame)
            print(self.face_detected)
            # Emit the frame regardless of face detection
            self.frameCaptured.emit(frame)

    def stop(self):
        self.running = False
        self.webcam.release()
        
    def is_face_detected(self):
        """Return whether a face was detected in the last frame"""
        return self.face_detected
    
    def reset_timer(self):
        """Reset the timer when face is not detected"""
        # This will be called from MainWindow to reset screen time tracking
        pass
