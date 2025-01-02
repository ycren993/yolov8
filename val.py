from ultralytics import YOLO
if __name__ == '__main__':
    # Load a model
    model = YOLO("/home/ycren/python/yolov8/runs/detect/BiFPN/weights/best.pt")

    # Customize validation settings
    validation_results = model.val(data="/home/ycren/python/URPC2020/data.yaml",imgsz=640,rect=False,classes=[0,1,2,3,4])
