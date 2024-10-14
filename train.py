from ultralytics import YOLO

def function():
    model = YOLO("yolov8m.pt")

    model.train(data="data_custom.yaml", batch=2, imgsz=640, epochs=50, workers=1)

def test():
    model = YOLO("yoloV8Custom.pt")

    model.predict(source = "1.jpg", show=True, conf=0.5)


if __name__ == '__main__':
    test()
