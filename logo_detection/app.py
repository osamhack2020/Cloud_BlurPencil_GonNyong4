from PIL import Image
import io
import torch
from flask import Flask, request
from flask_cors import CORS
from model import get_fasterrcnn_model, get_transform
app = Flask(__name__)
CORS(app)

config = dict()
model = None


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    print('/predict POST requested')
    file = request.files['file']
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    x = img2tensor(img)
    print('Now running model...')
    y = model(x)
    ret = dict()
    if len(y[0]['boxes']) > 0:
        from torchvision.ops import boxes as box_ops
        nms_idx = box_ops.nms(y[0]['boxes'], y[0]['scores'], iou_threshold=0.1)
        print('nms index:', nms_idx)
        print('left after nms: {:02f}%', len(nms_idx)*100/len(y[0]['boxes']))
        ret['boxes'] = y[0]['boxes'][nms_idx].tolist()
    else:
        ret['boxes'] = [[]]
    print('prediction complete')
    '''    
    ret = dict()
    # Assume we only serve one image per request
    ret['boxes'] = y[0]['boxes'].tolist()
    '''

    print(ret)
    return ret


def img2tensor(img):
    img = img.resize(config['img_size'])
    transform_f = get_transform(train=False)
    img = transform_f(img)
    x = [img]
    return x


if __name__ == '__main__':
    config['device'] = torch.device('cuda') \
        if torch.cuda.is_available() else torch.device('cpu')
    config['img_size'] = (224, 224)
    model = get_fasterrcnn_model(num_classes=2, verbose=True)
    model.eval()

    # x = img2tensor(Image.open('twice.jpg'))
    # y = model(x)
    # print('model test:', y)

    app.run(host='0.0.0.0', port=80)