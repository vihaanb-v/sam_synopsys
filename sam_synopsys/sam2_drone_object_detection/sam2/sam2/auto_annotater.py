from ultralytics.data.annotator import auto_annotate

auto_annotate(data="train/images", det_model="yolov8x.pt", sam_model = 'sam_b.pt', output_dir = " ")