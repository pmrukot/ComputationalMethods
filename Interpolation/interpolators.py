
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
