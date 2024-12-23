from typing import Callable
import math


type second = float
type speed = float
type step = float


def v(t: second) -> speed:
    return 3 * t**2 + 2 * t


def trapezoid(a: float, b: float, h: step,
              func: Callable[[float], float],
              step_error: float = .000001) -> float:
    if math.isclose(a, b, abs_tol=step_error):
        return .0

    limits_inverted: bool = False

    if a > b:
        limits_inverted = True
        a, b = b, a

    result: float = func(a) + func(b)

    for i in range(1, int((b - a + step_error) // h)):
        result += 2 * func(a + h * i)

    result *= h / 2

    if limits_inverted:
        result *= -1

    return result


def simpson(a: float, b: float, h: step,
            func: Callable[[float], float],
            step_error: float = .000001) -> float:
    if math.isclose(a, b, abs_tol=step_error):
        return .0

    limits_inverted: bool = False

    if a > b:
        limits_inverted = True
        a, b = b, a

    result: float = func(a) + func(b)
    amount_intervals: int = int((b - a + step_error) // h)

    if amount_intervals % 2:
        raise ValueError(f'Количество интервалов не четное ({amount_intervals} не четное)')

    for i in range(1, amount_intervals):
        result += (4 if i % 2 else 2) * func(a + h * i)

    result *= h / 3  # info! тоже самое, что 2 * h / 6

    if limits_inverted:
        result *= -1

    return result


if __name__ == '__main__':
    print(f'{trapezoid(0, 5, .1, v)=}')
    print(f'{simpson(0, 5, .1, v)=}')
