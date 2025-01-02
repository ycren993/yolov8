from ultralytics import YOLO
if __name__ == '__main__':
    # Load a model
    model = YOLO("/home/ycren/python/yolov8/runs/detect/SCDown/weights/last.pt")  # load a partially trained model
    # Resume training
    results = model.train(resume=True,patience=300)
