from ultralytics import YOLO
if __name__ == '__main__':
   model = YOLO("yolov8s-C2fGhost.yaml")
   results = model.train(data="/home/ycren/python/URPC2020/data.yaml", epochs=300,batch=32,optimizer="SGD",name='C2fGhost',patience=0)
# from ultralytics import YOLO
# if __name__ == '__main__':
    # # Load a model
    # model = YOLO("/home/ycren/python/yolov8/runs/detect/MobileViTv2-ECA/weights/last.pt")  # load a partially trained model
    # # Resume training
    # results = model.train(resume=True,patience=300)