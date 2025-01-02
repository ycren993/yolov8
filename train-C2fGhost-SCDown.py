from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s-C2fGhost-SCDown.yaml")
    results = model.train(data="/home/ycren/python/URPC2020/data.yaml", epochs=300, batch=32, optimizer="SGD",
                          name='C2fGhost-SCDown', patience=0)
