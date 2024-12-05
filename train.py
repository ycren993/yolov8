from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO("yolov8s-SCINet.yaml")
    results = model.train(data="E:/Python/ultralytics/ultralytics/cfg/datasets/uprc2018.yaml", epochs=300, project="E:/Python/ultralytics/runs",batch=16)