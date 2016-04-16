import numpy as np


def polynomial(x, i):
    return np.cos(x * i / 2) if i % 2 == 0 else np.sin(x * (i + 1) / 2)


def get_s_matrix(x, n):
    m = n + 1
    S = np.empty((m, m))
    indxs = range(m)

    for i in indxs:
        for j in indxs:
            S[i][j] = sum([polynomial(x[k], j) * polynomial(x[k], i) for k in range(len(x))])

    return S


def get_t_vector(points, n):
    x, y = zip(*points)
    m = n + 1
    t = []

    for i in range(m):
        sum = 0
        for j in range(len(x)):
            sum += polynomial(x[j], i) * y[j]
        t.append(sum)

    return t


def trigonometric_approximate(points, n):
    x, y = zip(*points)

    S = get_s_matrix(x, n)
    t = get_t_vector(points, n)

    A = np.linalg.solve(S, t)

    def function(x_point):
        result = 0
        for i in range(0, n+1):
            result += polynomial(x_point, i) * A[i]
        return result

    return function
