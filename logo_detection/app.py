from PIL import Image
import io
import torch
from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS
from model import get_fasterrcnn_model
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib import pyplot as plt
import utils
import config
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)
model = None

@app.route('/')
def demo():
    return render_template('test_clients/test_bbox')
    
@app.route('/about')
def about():
    return '''
    Logo Detection API Server
    Made by Seungpyo Hong [spkbk98 at gmail dot com]
    '''


@app.route('/blur', methods=['POST'])
def blur(context=None):
    if context is None:
        boxes = request.json['boxes']
        img = utils.extract_as_jpeg(request)
    else:
        boxes = context['boxes']
        img = context['image']

    img_crop = img.copy()
    img = np.array(img)
    img_crop = np.array(img_crop)
    print(img.shape)
    for xmin, ymin, xmax, ymax in boxes:
        xmin, ymin, xmax, ymax = \
            int(xmin), int(ymin), int(xmax), int(ymax)
        img_crop = cv2.blur(img_crop, (9, 9))
        img_crop[:ymin, :, :] = img[:ymin, :, :]
        img_crop[ymax:, :, :] = img[ymax:, :, :]
        img_crop[:, :xmin, :] = img[:, :xmin, :]
        img_crop[:, xmax:, :] = img[:, xmax:, :]
        img = img_crop
    fig, ax = plt.subplots(1)

    img = Image.fromarray((img).astype(np.uint8))
    ax.imshow(img)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/predict', methods=['POST'])
def predict():
    visualize = request.args.get('visualize', 'none')
    resize = request.args.get('resize', 'original')
    score_threshold = float(
        request.args.get('score_threshold', str(config.score_threshold)))
    nms_iou_threshold = float(
        request.args.get('nms_iou_threshold', str(config.nms_iou_threshold)))
    img = utils.extract_as_jpeg(request)

    x = utils.img2tensor(img, resize=True)

    x_original = utils.img2tensor(img, resize=False)
    scale = (
        x_original[0].size()[1] / x[0].size()[1],
        x_original[0].size()[2] / x[0].size()[2]
    )

    y = model(x)

    ret = dict()
    if len(y[0]['boxes']) > 0:
        ret = utils.post_process(
            y[0]['boxes'], y[0]['scores'], score_threshold, nms_iou_threshold)
        if resize == 'original':
            ret['boxes'] = utils.rescale_box(ret['boxes'], scale)
    else:
        ret['boxes'] = [[]]
        ret['scores'] = []

    if visualize == 'none':
        return jsonify(ret)
    img_to_show = x_original[0] if resize == 'original' else x
    if visualize == 'bbox':
        fig = utils.show_detection(img_to_show, ret['boxes'], pred_score=ret['scores'])
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
    elif visualize == 'blur':
        return blur({'boxes': ret['boxes'], 'image': img})


if __name__ == '__main__':
    config.device = torch.device('cuda') \
        if torch.cuda.is_available() else torch.device('cpu')
    model = get_fasterrcnn_model(num_classes=2)
    model.eval()

    app.run(host='0.0.0.0', port=80)