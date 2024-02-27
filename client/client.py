import requests


def main():
    resp = requests.get("http://localhost:8000/detections")
    print("Output image saved at:", resp.json()["output_image_path"])


if __name__ == "__main__":
    main()
