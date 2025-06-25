import cv2
import numpy as np

def extract_keyframes(video_path, interval=30):
    cap = cv2.VideoCapture(video_path)
    keyframes = []
    prev_frame = None
    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % interval == 0:
            if prev_frame is not None:
                diff = cv2.absdiff(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                                   cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY))
                if np.mean(diff) > 20:  
                    keyframes.append(frame)
            prev_frame = frame
        i += 1
    if not keyframes:
        print(f"No keyframes found in: {video_path} — using fallback frame.")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
        if ret:
            keyframes.append(frame)
    cap.release()
    return keyframes
