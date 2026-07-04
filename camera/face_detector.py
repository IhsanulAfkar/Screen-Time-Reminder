import cv2
import numpy as np
import numpy.typing as npt

from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp
from mediapipe import Image
class FaceDetector:
    def __init__(self, model_path: str = "models/face_landmarker.task"):
        base_options = python.BaseOptions(model_asset_path=model_path)

        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_faces=1,
            output_face_blendshapes=False,
            output_facial_transformation_matrixes=False,
        )

        self.detector = vision.FaceLandmarker.create_from_options(options)

    def detect(self, frame: np.ndarray):
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      mp_image = Image(
          image_format=mp.ImageFormat.SRGB,
          data=rgb
      )

      result = self.detector.detect(mp_image)

      if result.face_landmarks:
          return result.face_landmarks[0]

      return None
    def is_face_detected(self, frame: npt.NDArray[np.uint8]) -> bool:
        return self.detect(frame) is not None