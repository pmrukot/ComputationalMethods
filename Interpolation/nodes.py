import numpy as np

from function import fun


def get_regular_interpolation_nodes(n, start, end):
    return [(x, fun(x)) for x in np.linspace(start, end, n)]


def get_czebyshev_interpolation_nodes(n, start, end):
    points = []
    half_length = (end - start) / 2
    middle = start + half_length
    for i in range(0, n):
        x = middle + np.cos(((2 * i + 1) * np.pi) / (2 * n)) * half_length
        y = fun(x)
        points.append((x, y))
    return points
