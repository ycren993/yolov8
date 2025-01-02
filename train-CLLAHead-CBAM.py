from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s-CLLAHead-CBAM.yaml")
    results = model.train(data="/home/ycren/python/URPC2020/data.yaml", epochs=300, batch=32, optimizer="SGD",
                          name='CLLAHead-CBAM', patience=0)
