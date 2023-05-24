from ultralytics import YOLO
import cv2
import os

model = YOLO('runs/detect/yolov8x_kaidong_bs_8_lr0_0.0001_lrf_0.01/weights/best.pt')

os.mkdir('runs/detect/yolov8x_kaidong_bs_8_lr0_0.0001_lrf_0.01/predictions')

if __name__ == '__main__':
    prediction = model.predict(
        source="datasets/images/test2020/",
        conf=0.3,
        iou=0.5,
        device="cuda:0"
    )
    print(prediction)
