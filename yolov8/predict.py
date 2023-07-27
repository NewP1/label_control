from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO(r'C:\Users\user\yolov8\weight_files\weight_files\original_size_best')

# Define path to directory containing images and videos for inference
source = r'C:\Users\user\yolov8\val_resize\val_ori'

# Run inference on the source
results = model(source,save_txt=True,stream=True)  # generator of Results objects