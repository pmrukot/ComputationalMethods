import numpy as np
import matplotlib.pyplot as plt

from errors import print_error
from function import fun
from polynomial_approx import polynomial_approximate
from points import get_regular_interpolation_nodes, get_czebyshev_interpolation_nodes
from trigonometric_approx import trigonometric_approximate

if __name__ == '__main__':
    start = -2.*np.pi
    end = 1.*np.pi
    N = 7
    step = 0.05
    function = fun

    x = np.arange(start, end, step)
    y = list(map(function, x))

    x_len = len(x)

    #points = get_regular_interpolation_nodes(N, function, start, end)
    points = get_czebyshev_interpolation_nodes(N, function, start, end)

    x_nodes, y_nodes = zip(*points)

    polynomial = polynomial_approximate(points, N)
    trigonometric = trigonometric_approximate(points, N)

    polynomial_y = list(map(polynomial, x))
    trigonometric_y = list(map(trigonometric, x))

    print('label,N,mean_sqaure_error,max_error')
    print_error(N, x_len, y, polynomial_y, 'polynomial')
    print_error(N, x_len, y, trigonometric_y, 'trigonometric')

    plt.plot(x, y, "b--", linewidth=1, label='function')
    plt.plot(x, polynomial_y, "r--", linewidth=1, label='polynomial')
    plt.plot(x, trigonometric_y, "g--", linewidth=1, label='trigonometric')
    plt.plot(x_nodes, y_nodes, 'yo')
    plt.legend(loc='upper left', prop={'size': 8})
    plt.grid(True)
    plt.show()
