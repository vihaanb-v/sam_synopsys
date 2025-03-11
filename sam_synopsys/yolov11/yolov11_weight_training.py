from ultralytics import YOLO

weight_path = "/home/ubuntu/vihaan-devel/sam_synopsys/yolov11/runs/detect/train11/weights/best.pt"
#weight_path = "yolo11n.pt"

model = YOLO("yolo11n.yaml").load(weight_path)

results = model.train(data="/home/ubuntu/vihaan-devel/sam_synopsys/yolov11/datasets/dataset_fourth_round/data.yaml", epochs=25, imgsz=640, save=True, val=True)

#metrics = model.val(save_json=True, save_conf=True)