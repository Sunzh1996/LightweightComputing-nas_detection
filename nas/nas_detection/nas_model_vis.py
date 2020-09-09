import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# model
example_model = [
    'k3_e1',
    'k5_e6', 'skip', 'skip', 'k3_e3',
    'k7_e6', 'skip', 'k3_e6', 'k3_e6',
    'k7_e6', 'k7_e6', 'k5_e6', 'k3_e6',
    'k5_e6', 'skip', 'skip', 'k5_e3',
    'k5_e3', 'k7_e6', 'k7_e6', 'k7_e6',
    'k7_e6'
]
color_dict = {
    'k3_e1': [68, 113, 196],
    'k3_e3': [112, 173, 71],
    'k3_e6': [237, 125, 49],
    'k5_e3': [255, 192, 0],
    'k5_e6': [255, 52, 179],
    'k7_e3': [130, 130, 130],
    'k7_e6': [148, 0, 211],
    'skip':[220,13,33]

}

def plot_model(model, model_name):
    length = len(model)
    fig = plt.figure(figsize=(20, 5))
    ax = fig.add_subplot(1, 1, 1)

    # matrix config
    (m_width, m_height) = (1 / (2 * length + 2), 0.4)
    # line config
    l_width = m_width
    l_color = (0, 0, 0)
    # initial coordinate
    (x, y) = (l_width + 0.001, 0.4)

    # illustration
    x_i, y_i = (0.05, 0.1)
    for block in color_dict.keys():
        ax.add_patch(plt.Rectangle((x_i, y_i), 0.1, 0.1, fill=True, edgecolor=l_color,
                                   facecolor=tuple(x / 256 for x in color_dict[block]), linewidth=1))
        ax.text(x_i+0.017, y_i-0.1, block, fontsize=18, rotation=0)
        x_i += 0.12

    # input
    ax.add_line(plt.axhline(y=y + m_height / 2, xmin=0, xmax=l_width, linewidth=1, color=l_color))
    for block in model:
        ax.add_patch(plt.Rectangle((x, y), m_width, m_height, fill=True, edgecolor=l_color,
                                   facecolor=tuple(x / 256 for x in color_dict[block]), linewidth=1))
        ax.text(x+0.006, y+0.25, block, fontsize=18, rotation=90, color='white')

        ax.add_line(plt.axhline(y=y + m_height / 2, xmin=x + m_width + 0.001,
                                xmax=x + m_width + 0.001 + l_width, linewidth=1, color=l_color))
        #画stage竖直分割线
        plt.axvline(x=0.055, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.048, 0.91, '16', fontsize=16)
        plt.axvline(x=0.235, ymin=0.3, ymax=0.9, ls='--',color='black')
        ax.text(0.228, 0.91, '24', fontsize=16)
        plt.axvline(x=0.415, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.408, 0.91, '32', fontsize=16)
        plt.axvline(x=0.59, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.583, 0.91, '64', fontsize=16)
        plt.axvline(x=0.77, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.763, 0.91, '96', fontsize=16)
        plt.axvline(x=0.945, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.933, 0.91, '160', fontsize=16)
        plt.axvline(x=0.99, ymin=0.3, ymax=0.9, ls='--', color='black')
        ax.text(0.978, 0.91, '320', fontsize=16)

        (x, y) = (x + m_width + 0.001 + l_width, y)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),
                             'nas_detection/figure/{}.jpg'.format(model_name)))
    # plt.show()
    plt.cla()
    plt.close(fig)


if __name__ == '__main__':
    plot_model(example_model, model_name='model_example')
