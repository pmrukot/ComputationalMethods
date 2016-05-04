
def calculate_mean_square_error(x, f_y, f_i):
    n = len(x)
    return sum((f_y[i] - f_i[i])**2 for i in range(0, n)) / n


def calculate_max_error(x, f_y, f_i):
    return max(abs(f_y[i] - f_i[i]) for i in range(0, len(x)))
