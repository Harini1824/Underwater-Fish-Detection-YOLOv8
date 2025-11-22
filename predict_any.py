from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Select image using file dialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

if file_path:
    print(f"Predicting on: {file_path}")
    model.predict(
        source=file_path,
        show=True,
        save=True
    )
    print("Prediction complete. Check 'runs/detect/predict' folder.")
else:
    print("No file selected.")
