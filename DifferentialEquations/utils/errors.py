
def calculate_mean_square_error(x, f_y, f_i):
    n = len(x)
    mean_squared_error = 0
    for i in range(0, n):
        mean_squared_error += (f_y[i] - f_i[i])**2
    mean_squared_error /= n
    return mean_squared_error


def calculate_max_error(x, f_y, f_i):
    result = 0
    for i in range(0, len(f_y)):
        result = max(abs(f_y[i] - f_i[i]), result)
    return result
