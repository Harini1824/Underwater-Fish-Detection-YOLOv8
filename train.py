from ultralytics import YOLO

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")  # fastest for normal laptops

# Train the model
model.train(
    data="dataset/data.yaml",  # path to your dataset YAML file
    epochs=20,
    imgsz=640,
    workers=2
)
