import numpy as np


def fun(x):
    return np.exp(3*np.cos(2*x))


def fun_der(x):
    return -6.*np.sin(2*x)*np.exp(3*np.cos(2*x))
