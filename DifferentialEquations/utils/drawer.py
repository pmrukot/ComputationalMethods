from itertools import cycle

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

font = {'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 12,
        }

colors = cycle(cm.rainbow(np.linspace(0, 1, 4)))


def add_to_plot(x, y,label):
    plt.plot(x, y, "--",color=next(colors), label=label, linewidth=1.2)


def draw_plot(title, file_name):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 10
    fig_size[1] = 6
    plt.rcParams["figure.figsize"] = fig_size
    plt.legend(loc='upper left', prop={'size': 12})
    plt.title(title, fontdict = font)
    plt.grid(True)
    plt.show()
    plt.savefig("charts/" + file_name + '.png')
    plt.close()
