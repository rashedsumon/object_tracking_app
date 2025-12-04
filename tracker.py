"""
tracker.py
YOLO object detection + DeepSORT tracker for real-time tracking of 4 objects
"""

import cv2
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv8 model from ultralytics (can also use YOLOv5)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)

def track_objects(video_path):
    """
    Track exactly 4 visually similar objects in the given video
    """
    cap = cv2.VideoCapture(video_path)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO object detection
        results = model(frame)
        detections = []

        for *box, conf, cls in results.xyxy[0]:  # xyxy coordinates
            x1, y1, x2, y2 = map(int, box)
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf.item(), cls.item()))
        
        # Track using DeepSORT
        tracks = tracker.update_tracks(detections, frame=frame)
        
        # Draw tracks
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            l, t, w, h = track.to_ltrb()
            cv2.rectangle(frame, (int(l), int(t)), (int(w), int(h)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID:{track_id}', (int(l), int(t)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Tracking 4 Objects", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
