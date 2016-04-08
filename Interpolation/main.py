import numpy as np
import matplotlib.pyplot as plt

from errors import calculate_mean_square_error, calculate_max_error
from function import fun
from interpolators import lagrange_interpolate, newton_interpolate, hermit_interpolate
from nodes import get_regular_interpolation_nodes, get_czebyshev_interpolation_nodes


if __name__ == '__main__':
    start = -2.*np.pi
    end = 1.*np.pi
    N = 6
    x = np.arange(start, end, 0.1)
    x = np.append(x, end)
    print('nodes,Lagrange_sq,Newton_sq,Lagrange_max,Newton_max')

    points = get_regular_interpolation_nodes(N, start, end)
    #points = get_czebyshev_interpolation_nodes(N, start, end)

    lagrange_polynomial = lagrange_interpolate(points)
    newton_polynomial = newton_interpolate(points)
    hermit_polynomial = hermit_interpolate(points)

    function_y = [fun(x) for x in x]
    lagrange_y = [lagrange_polynomial(x) for x in x]
    newton_y = [newton_polynomial(x) for x in x]
    hermit_y = [hermit_polynomial(x) for x in x]

    x_points, y_points = zip(*points)

    print('{0},{1},{2},{3},{4}'.format(N,
         calculate_mean_square_error(x, function_y, lagrange_y), calculate_mean_square_error(x, function_y, newton_y),
         calculate_max_error(x, function_y, lagrange_y), calculate_max_error(x, function_y, newton_y)))

    print('{0},{1},{2}'.format(N,
                               calculate_mean_square_error(x, function_y, hermit_y),
                               calculate_max_error(x, function_y, hermit_y))
          )

    plt.plot(x, function_y, "r--", linewidth=2.0, label='function')
    plt.plot(x, lagrange_y, "g:", linewidth=2.5, label='lagrange')
    plt.plot(x, newton_y, "b--", linewidth=1.5, label='newton')
    plt.plot(x, hermit_y, "y--", linewidth=1.5, label='hermit')
    plt.plot(x_points, y_points, 'yo')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
    plt.grid(True)
    plt.show()
