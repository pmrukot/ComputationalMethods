import numpy as np


def get_points(n, start, end, function):
    points = []
    r = end - start
    step = r / n

    for i in np.arange(-2 * np.pi, 2 * np.pi, step):
        points.append((i, function(i)))
    points.append((end, function(end)))

    return points
