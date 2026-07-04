import mediapipe as mp

print("MediaPipe version:", mp.__version__)
print("Has Image:", hasattr(mp, "Image"))

if hasattr(mp, "Image"):
    print(dir(mp.Image))

print("\nTop-level members:")
print([x for x in dir(mp) if "Image" in x or "image" in x])