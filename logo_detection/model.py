import torch
import torchvision
import torchvision.transforms as T
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import config


def collate_fn(batch):
    return tuple(zip(*batch))


def get_transform(train):
    transforms = list()
    # transforms = [T.Resize((H, W), interpolation=2)]
    transforms.append(T.ToTensor())
    '''
    if train:
        transforms.append(T.RandomHorizontalFlip(0.5))
    '''
    return T.Compose(transforms)
# https://pytorch.org/tutorials/intermediate/torchvision_tutorial.html


def get_fasterrcnn_model(num_classes, use_custom=True):
    if use_custom:
        if config.verbose:
            print('Loading custom weight file:', config.model_path)
        return torch.load(config.model_path, map_location=torch.device('cpu'))
    
    if config.verbose:
        print('Loading pretrained Faster R-CNN...')
    # load a model pre-trained pre-trained on COCO
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=False)
    if config.verbose:
        print('Loaded Pretrained Faster R-CNN')
    # get number of input features for the classifier
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model


