import numpy as np


def calculate_mean_square_error(n, function_y, interpolated_y):
    error = 0
    for i in range(0, n):
        error += (function_y[i] - interpolated_y[i])**2
    error /= n
    return error


def calculate_max_error(n, function_y, interpolated_y):
    max_error = 0
    for i in range(0, n):
        if np.fabs(function_y[i] - interpolated_y[i]) > max_error:
            max_error = np.fabs(function_y[i] - interpolated_y[i])
    return max_error


def print_error(N, x_len, y_values, y_interpolated, label):
    print('{0},{1},{2},{3}'.format(label, N,
                                   calculate_mean_square_error(x_len, y_values, y_interpolated),
                                   calculate_max_error(x_len, y_values, y_interpolated)
                                   ))
