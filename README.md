# Underwater-Fish-Detection-YOLOv8
Underwater Fish Detection using YOLOv8

This project uses a custom-trained YOLOv8 object detection model to detect underwater fish species.
The model is trained on a dataset from Roboflow and fine-tuned using the Ultralytics YOLOv8 framework.

#Training the Model

Run:

python train.py


The trained model will be saved in:

runs/detect/train/weights/best.pt

#Running Predictions

Run:

python predict_any.py


A file picker will open → select any JPG/PNG image → output appears automatically and is saved in:

runs/detect/predict2/

Model Used

YOLOv8n (pretrained on COCO, fine-tuned on custom dataset)

Framework: Ultralytics YOLOv8

Augmentation: Handled internally by YOLO

Requirements
ultralytics
pillow
tk

