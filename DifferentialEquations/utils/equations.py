import numpy as np


def calculate_f_x_1(x, k=3, m=1):
    return np.exp((-k) * np.cos(m * x)) - k * np.cos(m * x) + 1


def calculate_differential_equation(x, y, k=0, m=0):
    return k*k*m*np.sin(m*x)*np.cos(m*x) + k*m*y*np.sin(m*x)


@np.vectorize
def calculate_f_x_2b(x, k, m):
    return np.cos(m*x)-x*np.sin(m*x)


@np.vectorize
def calculate_differential_equation_2a(x, k, m):
    return -2*m*np.cos(m * x)
