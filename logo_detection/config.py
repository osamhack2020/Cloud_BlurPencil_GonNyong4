import os
import torch

verbose = True
model_dir = '/workspace/OSAM2020_4GB/Cloud_BlurPencil_GonNyong4/logo_detection/weights'
model_file = 'model_epoch_10.pth'
model_path = os.path.join(model_dir, model_file)
img_size = (224, 224)
device = torch.device('cpu')