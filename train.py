from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO("yolov8s-AFPN.yaml")
    results = model.train(data="D:\PythonFile\datasets\\URPC.v1i.yolov8\data.yaml", epochs=300, project="E:/Python/ultralytics/runs",batch=8)