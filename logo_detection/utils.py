import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision import transforms
import torch
from torchvision.ops import boxes as box_ops
import requests
from model import get_transform
import config
from PIL import Image
import io
from werkzeug.utils import secure_filename
import numpy as np


def img2tensor(img, resize=True):
    if resize:
        img = img.resize(config.img_size)
    transform_f = get_transform(train=False)
    img = transform_f(img)
    x = [img]
    return x


def extract_as_jpeg(request):
    if 'file' not in request.files:
        raise Exception('No file part')
    file = request.files['file']
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))

    # Read image as JPEG format.
    filename = secure_filename(file.filename)
    extension = filename.split('.')[-1]
    # https://stackoverflow.com/a/48970633
    if extension == 'jpg' or extension == 'jpeg':
        pass
    else:
        f = io.BytesIO()
        img.convert('RGB').save(f, format='JPEG')
        f.seek(0)
        img = Image.open(f)
    return img


def rescale_box(boxes, scale):
    '''
    boxes: [[xmin, ymin, xmax, ymax], [xmin, ymin, xmax, ymax], ...]
    scale: [y(height)_scale, x(width)_ratio]
    '''
    for i, _ in enumerate(boxes):
        boxes[i][0] *= scale[1]
        boxes[i][2] *= scale[1]
        boxes[i][1] *= scale[0]
        boxes[i][3] *= scale[0]
    return boxes


def post_process(boxes, scores, score_threshold, nms_iou_threshold):
    ret = dict()
    confident_idx = np.where(scores > score_threshold)
    ret['boxes'] = boxes[confident_idx]
    ret['scores'] = scores[confident_idx]
    nms_idx = box_ops.nms(
        ret['boxes'], ret['scores'], nms_iou_threshold)
    ret['boxes'] = ret['boxes'][nms_idx].tolist()
    ret['scores'] = ret['scores'][nms_idx].tolist()
    return ret


def show_detection(x, pred, gt=None, pred_score=None, pred_color='r', gt_color='g'):
    '''
    Arguements:
    x : Tensor of a single image
    bbox : Tensor
    '''
    fig, ax = plt.subplots(1)
    plt.axis('off')
    plt.margins(0, 0)
    if isinstance(x, torch.Tensor):
        img = transforms.ToPILImage()(x).convert("RGB")
    ax.imshow(img)
    if pred is not None:
        for i, p in enumerate(pred):
            rect = patches.Rectangle(
                (p[0], p[1]), p[2]-p[0], p[3]-p[1], linewidth=2,
                edgecolor=pred_color, facecolor='none')
            ax.add_patch(rect)
            if pred_score is not None:
                ax.text(p[0], p[1], str(round(pred_score[i]*100, 2))+'%')
    if gt is not None:
        for g in gt:
            rect = patches.Rectangle(
                (g[0], g[1]), g[2]-g[0], g[3]-g[1], linewidth=2,
                edgecolor=gt_color, facecolor='none')
            ax.add_patch(rect)
    return fig


# https://stackoverflow.com/a/39225039
def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)

