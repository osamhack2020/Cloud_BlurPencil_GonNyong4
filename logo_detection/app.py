from PIL import Image
import io
import torch
from torchvision.ops import boxes as box_ops
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
from model import get_fasterrcnn_model
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import utils, config

app = Flask(__name__)
CORS(app)
model = None


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify('No file part')
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

    x = utils.img2tensor(img)
    y = model(x)

    ret = dict()
    if len(y[0]['boxes']) > 0:
        nms_idx = box_ops.nms(y[0]['boxes'], y[0]['scores'], iou_threshold=0.1)
        # print('nms index:', nms_idx)
        # print('left after nms: {:02f}%', len(nms_idx)*100/len(y[0]['boxes']))
        ret['boxes'] = y[0]['boxes'][nms_idx].tolist()
    else:
        ret['boxes'] = [[]]

    visualize = request.args.get('visualize', 'none')
    if visualize == 'none':
        return jsonify(ret)
    if visualize == 'bbox':
        fig = utils.show_detection(x[0], ret['boxes'])
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    config.device = torch.device('cuda') \
        if torch.cuda.is_available() else torch.device('cpu')
    model = get_fasterrcnn_model(num_classes=2)
    model.eval()

    app.run(host='0.0.0.0', port=80)