import numpy as np


def calculate_cubic_value(t, y):
    n = len(t)
    h = []
    b = []
    u = [0]
    v = [0]

    for i in range(0, n - 1):
        h.append(t[i + 1] - t[i])
        b.append(6 * (y[i + 1] - y[i]) / h[i])

    u.append(2 * (h[0] + h[1]))
    v.append(b[1] - b[0])

    for i in range(2, n - 1):
        u.append(2 * (h[i - 1] + h[i]) - (h[i - 1] * h[i - 1]) / u[i - 1])
        v.append((b[i] - b[i - 1]) - (h[i - 1] * v[i - 1] / u[i - 1]))

    z = [0] * (n)

    for i in range(n - 2, 0, -1):
        z[i] = ((v[i] - h[i] * z[i + 1]) / u[i])

    z[0] = 0
    return z, h


def calculate_cubic_value_not_a_knot(t, y):
    n = len(t)
    h = []
    b = []
    v = [0]
    A = np.zeros(shape=(n, n))

    for i in range(0, n - 1):
        h.append(t[i + 1] - t[i])
        b.append(6 * (y[i + 1] - y[i]) / h[i])

    A[0][0] = h[1]
    A[0][1] = - h[1] - h[0]
    A[0][2] = h[0]

    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        v.append(b[i] - b[i - 1])

    v.append(0)
    A[n - 1][n - 3] = h[n - 2]
    A[n - 1][n - 2] = - h[n - 2] - h[n - 3]
    A[n - 1][n - 1] = h[n - 3]

    z = np.linalg.solve(A, v)

    return z, h


def create_cubic_function(t, y, calc):
    z, h = calc(t, y)

    def spline_function(x):
        i = 0
        while float(x) - t[i] >= 0:
            i += 1
        i -= 1
        A = (z[i + 1] - z[i]) / (6 * h[i])
        B = z[i] / 2.
        C = -(h[i] * (z[i + 1] + 2 * z[i])) / 6 + (y[i + 1] - y[i]) / h[i]
        return y[i] + ((x - t[i]) * (C + (x - t[i]) * (B + (x - t[i]) * A)))

    return spline_function
