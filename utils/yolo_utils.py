from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

def detect_objects(frame, conf=0.4):
    """
    Runs object detection on a frame using YOLOv8.
    Returns list of detections with (label, confidence, (x1, y1, x2, y2))
    """
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = model.predict(source=img_rgb, conf=conf, save=False, verbose=False)

    detections = []
    if results and results[0].boxes:
        for box in results[0].boxes:
            label_idx = int(box.cls[0])
            label = model.names[label_idx]
            confidence = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            detections.append((label, confidence, (int(x1), int(y1), int(x2), int(y2))))

    return detections
