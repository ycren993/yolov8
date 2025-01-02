from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO("yolov8s.yaml")
    results = model.train(data="/home/ycren/python/URPC2021enchanced/data.yaml", epochs=300, batch=32, optimizer="SGD",
                          name='baseline-enchanced', patience=0,amp=False)
