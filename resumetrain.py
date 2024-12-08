from ultralytics import YOLO
if __name__ == '__main__':
    # Load a model
    model = YOLO("parameter/yolov10s_colab_20241208_1630_last.pt")  # load a partially trained model

    # Resume training
    results = model.train(resume=True)