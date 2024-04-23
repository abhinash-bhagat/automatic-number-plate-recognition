# License Plate Detection and Text Extraction

This project utilizes YOLO (You Only Look Once) for license plate detection and EasyOCR for text extraction from license plates. The YOLO model is fine-tuned 
on a custom dataset to detect license plates accurately.

## Overview

The project consists of the following main components:
- **YOLO Model Training**: Fine-tuning the YOLO model on a custom dataset containing images with annotated license plates.
- **License Plate Detection**: Using the trained YOLO model to detect license plates in images or videos.
- **Text Extraction**: Utilizing EasyOCR to extract text from the detected license plates.

## Usage

To use the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/automatic-number-plate-recognition.git
   cd license-plate-detection

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Training Script** (Get your own dataset):
   ```bash
   yolov9/solution.ipynb

4. **Run the detection Script**:
   ```bash
   yolov9/solution.ipynb

## Acknowledgements

    YOLOv5 Official Repository: https://github.com/ultralytics/yolov5
    YOLOv5 Official Repository: https://github.com/WongKinYiu/yolov9
    EasyOCR Repository: https://github.com/JaidedAI/EasyOCR
