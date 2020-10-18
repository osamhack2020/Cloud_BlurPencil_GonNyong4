import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision import transforms


def show_detection(x, pred, gt=None, pred_color='r', gt_color='g'):
    '''
    Arguements:
    x : Tensor
    bbox : Tensor
    '''
    print('show_detection: x:', x)
    print('show_detection: x.size() = ', x.size())
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
    '''
        plt.show()
    for rect in toClear:
        rect.remove()
    '''
