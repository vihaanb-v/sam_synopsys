import os

print(os.getcwd())

for i in range(13):
    i = i + 3
    os.system('cp /home/ubuntu/vihaan-devel/sam_synopsys/yolov11/runs/detect/train' + str(i) + '/confusion_matrix_normalized.png /home/ubuntu/vihaan-devel/sam_synopsys/yolov11/confusion_matrices/confusion_matrix_normalized_train' + str(i) + '.png')