from dataclasses import dataclass
from typing import Callable


@dataclass(slots=True)
class Point:
    x: float = 0
    y: float = 0

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x:.2f}, y={self.y:.2f})'


type step = float
type points = list[Point]


def function(_: float, y: float) -> float:
    k: float = .07
    t_e: float = 20.0

    return k * (t_e - y)


def found_with_improved_euler(start_point: Point,
                              desired_y: float,
                              search_step: step,
                              func: Callable[[float, float], float],
                              max_search_iterations: int = 10_000) -> points:
    result_points: points = []
    current_proximity_to_desired: float = abs(desired_y - start_point.y)
    next_current_proximity_to_desired: float = .0

    if current_proximity_to_desired < search_step:
        return []

    result_points.append(start_point)

    while True:
        current_point: Point = result_points[-1]

        a_i: float = current_point.x + search_step / 2
        b_i: float = func(current_point.x, current_point.y)
        c_i: float = current_point.y + search_step / 2 * b_i
        d_i: float = func(a_i, c_i)
        delta_y: float = search_step * d_i

        next_point: Point = Point(current_point.x + search_step, current_point.y + delta_y)

        next_current_proximity_to_desired = abs(desired_y - next_point.y)

        if next_current_proximity_to_desired > current_proximity_to_desired:
            break

        current_proximity_to_desired = next_current_proximity_to_desired
        result_points.append(next_point)

        if len(result_points) > max_search_iterations:
            raise StopIteration(f'Количество итераций превысило предел в {max_search_iterations}')

    return result_points


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import pprint

    input_start_point: Point = Point(0, 100.0)
    input_desired_y: float = 30.0
    input_search_step: float = 1

    result: points = found_with_improved_euler(input_start_point, input_desired_y, input_search_step, function)

    pprint.pprint(result, width=40)

    plt.title('Решения ОДУ с помощью уточнённой схемы Эйлера')
    plt.xlabel('минуты')
    plt.ylabel('°C')
    plt.legend(('пройденные точки'))

    list_x: list[float] = []
    list_y: list[float] = []
    list_y_function: list[float] = []
    start: float = 100.0

    for i, el in enumerate(result):
        list_x.append(el.x)
        list_y.append(el.y)

        list_y_function.append(start)
        start += function(0, start)

    plt.plot(list_x, list_y, marker='o', linestyle='solid')
    plt.plot(list_x, list_y_function)

    plt.legend(['пройденные точки', 'функция'], loc='upper right')

    plt.grid()
    plt.show()
