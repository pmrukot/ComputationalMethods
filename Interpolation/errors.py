import numpy as np


def calculate_mean_square_error(x, function_y, interpolated_y):
    n = len(x)
    error = 0
    for i in range(0, n):
        error += (function_y[i] - interpolated_y[i])**2
    error /= n
    return error


def calculate_max_error(x, function_y, interpolated_y):
    n = len(x)
    max_error = 0
    for i in range(0, n):
        if np.fabs(function_y[i] - interpolated_y[i]) > max_error:
            max_error = np.fabs(function_y[i] - interpolated_y[i])
    return max_error
