import numpy as np


def fun(x, k=3, m=1):
    return np.exp((-k) * np.sin(m * x)) + k * np.sin(m * x) - 1
