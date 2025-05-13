import cv2
import numpy as np
from ultralytics import YOLO

class PeopleCounter:
    def __init__(self, model_path="Kelompok2Model.pt"):
        self.model = YOLO(model_path)

    def process_frame(self, frame):
        results = self.model(frame)[0]
        count = 0
        annotated_frame = frame.copy()

        for box in results.boxes:
            cls = int(box.cls[0])
            if self.model.names[cls] == 'person':
                count += 1
                xyxy = box.xyxy[0].cpu().numpy().astype(int)
                cv2.rectangle(annotated_frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'Person', (xyxy[0], xyxy[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return annotated_frame, count