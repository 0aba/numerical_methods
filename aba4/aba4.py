from typing import Callable
import math


type step = float

type row_x = list[float]
type row_y = list[float]
type points = [row_x, row_y]


def function(x: float) -> float:
    return 4 * math.cos(2*x)


def approximate_derivative(func: Callable[[float], float],
                           x: float,
                           delta: float = .000001) -> float:
    return (func(x + delta) - func(x)) / delta


def parabolic_splines(start_points: points,
                      h: step,
                      func: Callable[[float], float],
                      step_error: float = .000001) -> points:
    result_points: points = [[], []]

    for i in range(int((start_points[0][-1] - start_points[0][0] + step_error) // h) + 1):
        result_points[0].append(start_points[0][0] + h * i)
        result_points[1].append(.0)

    current_top_point: int = 0
    x_i: float = 0
    a_i: float = 0
    b_i: float = 0
    next_b_i: float = 0
    c_i: float = 0

    for i in range(len(result_points[0])):
        if result_points[0][i] >= start_points[0][current_top_point] and current_top_point < len(start_points[0]) - 1:
            current_top_point += 1

            x_i = start_points[0][current_top_point - 1]
            y_i: float = start_points[1][current_top_point - 1]
            next_x_i: float = start_points[0][current_top_point]
            next_y_i: float = start_points[1][current_top_point]

            h_i: float = next_x_i - x_i
            a_i = y_i
            b_i = approximate_derivative(func, x_i) if not i else next_b_i

            z_i: float = (2*(next_y_i - y_i)) / h_i
            next_b_i = z_i - b_i
            c_i = (next_b_i - b_i) / (2 * h_i)

        x: float = result_points[0][i]
        result_points[1][i] = a_i + b_i * (x - x_i) + c_i * (x - x_i)**2

    return result_points


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    delta_h: float = .2
    input_points: points = [[44, 44.66, 45.33, 46],
                            [4, 0.85, -3.61, -2.51]]

    result: points = parabolic_splines(input_points, delta_h, function)

    print(f'row x={result[0]}\n'
          f'row y={[round(x, 2) for x in result[1]]}')

    plt.title('Метод параболических сплайнов')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.plot(result[0], result[1], marker='o', linestyle='dotted')

    plt.grid()
    plt.show()







# def lagrange_polynomial(start_points: points, x: float):
#     n: int = len(start_points[0])
#     result: int = 0
#
#     for i in range(n):
#         polynomial = 1
#
#         for j in range(n):
#             if i != j:
#                 polynomial *= (x - start_points[0][j])/(start_points[0][i] - start_points[0][j])
#
#         result += start_points[1][i] * polynomial
#
#     return result