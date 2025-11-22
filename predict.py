from ultralytics import YOLO

# Load your trained model (best weight)
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction on an image
model.predict(
    source="test.jpg",   # change this to any image you want to test
    show=True,
    save=True
)
