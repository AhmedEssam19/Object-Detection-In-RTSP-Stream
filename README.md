# Object-Detection-In-RTSP-Stream

## Description
This project is a simple example of how we can detect object in a RTSP stream (Camera) using YOLOv5 and OpenCV.

## Details
The project is divided into three parts:
1. Simulated RTSP Stream (Camera): Using RTSP Server ([mediamtx](https://github.com/bluenviron/mediamtx)) and `ffmpeg` that streams a fixed video on repeat. 
`ffmpeg` acts as a RTSP publisher.
2. Inference Server: A simple Flask server that uses YOLOv5 to detect objects in the RTSP stream and saves the image with detection boxes when receiving `GET` request. The server acts as a RTSP listener. Additionally, Gunicorn is used as an application server for efficiency.
3. Client: A simple Python script that sends `GET` request to the Inference Server to get the path of the saved image.

![Solution Design](http://url/to/img.png)

## Usage
1. Clone the repository.
```shell
$ git clone https://github.com/AhmedEssam19/Object-Detection-In-RTSP-Stream.git
$ cd Object-Detection-In-RTSP-Stream
```
2. Start the RTSP and inference servers.
```shell
$ export HOST_OUTPUT_FOLDER_PATH=[PATH TO DESIRED FOLDER] WEIGHT_FILE=[WEIGHT FILE NAME OF DESIRED VERSION e.g., yolov5xu.pt, yolov5s.pt, ...etc]
$ docker compose up
```
3. Run the client code.
```shell
$ cd client
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 client.py
```

## Prerequisites
* Nvidia Drivers
* Docker
* Nvidia Container Toolkit
* python3 with venv