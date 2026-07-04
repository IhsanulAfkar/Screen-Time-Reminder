import cv2
class Webcam:
    def __init__(self, camera_index: int = 0):
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise RuntimeError("Unable to open webcam.")

    def read(self):
        """
        Returns:
            (success, frame)
        """
        return self.cap.read()

    def release(self):
        if self.cap.isOpened():
            self.cap.release()