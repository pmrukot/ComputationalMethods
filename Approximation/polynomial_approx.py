import numpy as np


def get_s_matrix(x, n):
    m = n + 1
    S = np.empty((m, m))

    for i in range(m):
        for j in range(m):
            S[i][j] = (sum([x**(i+j) for x in x]))

    return S


def get_t_vector(points, n):
    m = n + 1
    t = []

    for i in range(m):
        t.append(sum([y*(x**i) for x, y in points]))

    return t


def polynomial_approximate(points, n):
    x, y = zip(*points)

    S = get_s_matrix(x, n)
    t = get_t_vector(points, n)

    A = np.linalg.solve(S, t)

    def function(x_point):
        result = 0
        for i in range(0, n+1):
            result += (x_point**i) * A[i]
        return result

    return function
