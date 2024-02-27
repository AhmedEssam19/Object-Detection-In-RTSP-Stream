import os
import cv2
import torch

from uuid import uuid4
from flask import Flask
from ultralytics import YOLO

app = Flask(__name__)


@app.route("/detections", methods=['GET'])
def get_detections():
    model = YOLO(os.getenv("WEIGHT_PATH"), task="detection")
    cap = cv2.VideoCapture("rtsp://rtsp-server:8554/stream")
    ret, frame = cap.read()
    results = model(frame)
    filename = str(uuid4()) + ".jpg"
    results[0].save(os.path.join("outputs", filename))

    cap.release()
    torch.cuda.empty_cache()

    return {"output_image_path": os.path.join(os.getenv("HOST_OUTPUT_FOLDER_PATH"), filename)}


if __name__ == "__main__":
    app.run()
