import numpy as np


def calculate_quadratic_value(t, y):
    n = len(t)
    z = [0]

    for i in range(0, n - 1):
        z.append(-z[i] + 2 * ((y[i + 1] - y[i]) / (t[i + 1] - t[i])))
    return z


def calculate_quadratic_value_not_a_knot(t, y):
    n = len(t)
    d = [(y[1] - y[0]) / (t[1] - t[0])]
    A = np.zeros(shape=(n, n))
    A[0][0] = 1

    for i in range(1, n):
        A[i][i-1] = 1
        A[i][i] = 1
        d.append(2 * ((y[i] - y[i-1]) / (t[i] - t[i-1])))

    return np.linalg.solve(A, d)


def create_quadratic_function(t, y, calc):
    z = calc(t, y)

    def spline_function(x):
        i = 0
        while x - t[i] >= 0:
            i += 1
        i -= 1
        return ((z[i + 1] - z[i]) * (x - t[i]) * (x - t[i])) / (2 * (t[i + 1] - t[i])) + z[i] * (x - t[i]) + y[i]

    return spline_function
