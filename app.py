from flask import Flask, request, jsonify, send_file, url_for
from ultralytics.yolo.engine.model import YOLO

import cv2

model_path = r"yoloV8Custom.pt"
model = YOLO(model_path)

app = Flask(__name__)



@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    print(image_file)
    image_file.save('image.jpg')
    img=cv2.imread('image.jpg')
    results = model.predict(stream=True, imgsz=640, source=img, save=True)
    response = []
    for r in results:
        for c in r.boxes.cls:
            response.append(model.names[int(c)])
    return jsonify(response)

# @app.route('/download')
# def download_file():
#     path = r"C:\\Users\\muham\Downloads\\object detection dice\\runs\\detect\\predict2\\image0.jpg"
#     return send_file(path, as_attachment=True)

@app.route('/image')
def get_image():
    filename = r"C:\\Users\\muham\Downloads\\object detection dice\\runs\\detect\\predict2\\image0.jpg"
    return filename


app.run(host='0.0.0.0', port=5000)
