import os
import torch

'''
Default configuration values.
NEVER MODIFY VALUES IN THIS FILE PROGRAMMATICALLY!
'''

verbose = True
model_dir = '/workspace/OSAM2020_4GB/Cloud_BlurPencil_GonNyong4/logo_detection/weights'
model_file = 'model_trainsize_2000_epoch_13.pth'
model_path = os.path.join(model_dir, model_file)
img_size = (224, 224)
device = torch.device('cpu')
score_threshold = 0.5
nms_iou_threshold = 0.2