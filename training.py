from ultralytics import YOLO

model = YOLO('yolov5m.pt')
model.train(data = 'configure.yaml', epochs = 1, imgsz = 640)