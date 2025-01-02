from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s-BiFPN.yaml")
    results = model.train(data="/home/ycren/python/URPC2020/data.yaml", epochs=300, batch=32, optimizer="SGD",
                          name='BiFPN', patience=0,amp=False)
