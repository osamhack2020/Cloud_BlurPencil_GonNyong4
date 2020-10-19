import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision import transforms
import requests
from model import get_transform
import config


def img2tensor(img):
    img = img.resize(config.img_size)
    transform_f = get_transform(train=False)
    img = transform_f(img)
    x = [img]
    return x


def show_detection(x, pred, gt=None, pred_color='r', gt_color='g'):
    '''
    Arguements:
    x : Tensor of a single image
    bbox : Tensor
    '''
    fig, ax = plt.subplots(1)
    img = transforms.ToPILImage()(x).convert("RGB")
    ax.imshow(img)
    toClear = list()
    if pred is not None:
        for p in pred:
            rect = patches.Rectangle(
                (p[0], p[1]), p[2]-p[0], p[3]-p[1], linewidth=2,
                edgecolor=pred_color, facecolor='none')
            ax.add_patch(rect)
            toClear.append(rect)
    if gt is not None:
        for g in gt:
            rect = patches.Rectangle(
                (g[0], g[1]), g[2]-g[0], g[3]-g[1], linewidth=2,
                edgecolor=gt_color, facecolor='none')
            ax.add_patch(rect)
            toClear.append(rect)
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

