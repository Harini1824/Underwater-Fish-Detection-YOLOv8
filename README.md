# Underwater Fish Detection using YOLOv8

This project uses a custom-trained **YOLOv8** object detection model to detect underwater fish species.
The model is trained on a dataset from **Roboflow** and fine-tuned using the **Ultralytics YOLOv8 framework**.

## Training the Model

Run the following command to start training:

```bash
python train.py
```

The trained model will be saved in:

```
runs/detect/train/weights/best.pt
```

## Running Predictions

Run the following command to make predictions:

```bash
python predict_any.py
```

* A file picker will open → select any JPG/PNG image.
* The output will appear automatically and is saved in:

```
runs/detect/predict2/
```

## Model Used

* **Model:** YOLOv8n (pretrained on COCO, fine-tuned on custom dataset)
* **Framework:** Ultralytics YOLOv8
* **Augmentation:** Handled internally by YOLO

## Requirements

* `ultralytics`
* `pillow`
* `tkinter`
