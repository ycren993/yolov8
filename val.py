from ultralytics import YOLO
if __name__ == '__main__':
    # Load a model
    model = YOLO("/home/ycren/python/yolov8/runs/detect/yolov8n/weights/best.pt")

    # Customize validation settings
    validation_results = model.val(data="/home/ycren/python/URPC2020/data.yaml",imgsz=640)
