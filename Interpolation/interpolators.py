import numpy as np

from function import fun_der


def lagrange_interpolate(points):
    def result_polynomial(x):
        sum = 0
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            product = 1
            for j in range(n):
                if i != j:
                    xj, yj = points[j]
                    product *= (x - xj) / float(xi - xj)
            sum += yi*product
        return sum
    return result_polynomial


def newton_interpolate(points):
    x1, y1 = zip(*points)
    n = len(points)
    dq = list(y1)
    x = list(x1)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            dq[j] = (dq[j] - dq[j - 1]) / (x[j] - x[j - i])

    def result_polynomial(xpoint):
        val = dq[0]
        factor = 1.0
        for i in range(1, n):
            factor *= (xpoint - x[i - 1])
            val += (dq[i] * factor)
        return val

    return result_polynomial


def hermit_interpolate(points):
    x, y = zip(*points)
    n = len(points)
    x, y = list(x), list(y)

    hermit_matrix = np.zeros(shape=(2*n+1, 2*n+1))

    # 2*(2n) places in matrix are function values and derivative values
    # then we will add diffrences quotients later
    for i in range(0, 2*n, 2):
        hermit_matrix[i][0], hermit_matrix[i+1][0] = x[i//2], x[i//2]
        hermit_matrix[i][1], hermit_matrix[i+1][1] = y[i//2], y[i//2]


    # now we add values of function derivative and quotient diffrences
    # this is nearlny lower triangular matrix
    for i in range(2, 2*n+1):
        for j in range(1 + (i - 2), 2*n):
            if i == 2 and j % 2 == 1:
                hermit_matrix[j][i] = fun_der(x[j//2])
            else:
                hermit_matrix[j][i] = (
                                          hermit_matrix[j][i - 1] - hermit_matrix[j - 1][i - 1]
                                      ) / (
                                          hermit_matrix[j][0] - hermit_matrix[(j - 1) - (i - 2)][0]
                                      )

    #calculate value for given x
    def result_polynomial(xpoint):
        value = 0
        for i in range(0, 2 * n):
            factor = 1.
            j = 0
            while j < i:
                factor *= (xpoint - x[j//2])
                if j + 1 != i:
                    factor *= (xpoint - x[j//2])
                    j += 1
                j += 1
            value += factor * hermit_matrix[i][i + 1]
        return value

    return result_polynomial
