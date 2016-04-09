import numpy as np
import matplotlib.pyplot as plt

from cubic_splines import calculate_cubic_value, create_cubic_function, calculate_cubic_value_not_a_knot
from quadratic_splines import create_quadratic_function, calculate_quadratic_value, calculate_quadratic_value_not_a_knot
from function import fun
from errors import print_error
from points import get_points


if __name__ == '__main__':
    start = -2.*np.pi
    end = 2.*np.pi
    step = 0.05
    N = 8
    function = fun

    points = get_points(N-1, start, end, function)

    x_points, y_points = zip(*points)

    x = np.arange(start, end, step)
    y = [function(x) for x in x]
    x_len = len(x)

    quadratic_spline_natural = create_quadratic_function(x_points, y_points, calculate_quadratic_value)
    quadratic_spline_notaknot = create_quadratic_function(x_points, y_points, calculate_quadratic_value_not_a_knot)
    cubic_spline_natural = create_cubic_function(x_points, y_points, calculate_cubic_value)
    cubic_spline_not_a_knot = create_cubic_function(x_points, y_points, calculate_cubic_value_not_a_knot)

    quadratic_spline_natural_values = [quadratic_spline_natural(x) for x in x]
    quadratic_spline_notaknot_values = [quadratic_spline_notaknot(x) for x in x]
    cubic_spline_natural_values = [cubic_spline_natural(x) for x in x]
    cubic_spline_notaknot_values = [cubic_spline_not_a_knot(x) for x in x]

    print('label,N,mean_sqaure_error,max_error')
    print_error(N, x_len, y, quadratic_spline_natural_values, 'quadratic_natural')
    print_error(N, x_len, y, quadratic_spline_notaknot_values, 'quadratic_notaknot')
    print_error(N, x_len, y, cubic_spline_natural_values, 'cubic_natural')
    print_error(N, x_len, y, cubic_spline_notaknot_values, 'cubic_notaknot')

    plt.plot(x, function(x), 'b', linewidth=2.5, label="function")
    plt.plot(x, cubic_spline_natural_values, 'r--', linewidth=2.5, label='cubic natural')
    plt.plot(x, cubic_spline_notaknot_values, 'r--', color='#880000', linewidth=2.5, label='cubic notaknot')
    plt.plot(x, quadratic_spline_natural_values, 'g--', linewidth=2.5, label='quad natural')
    plt.plot(x, quadratic_spline_notaknot_values, 'g--', color='#808000', linewidth=2.5, label='quad notaknot')
    plt.plot(x_points, y_points, 'yo')
    plt.legend(loc='upper left')
    plt.show()
