from typing import Callable

type seconds = float
type height = float


def h(t: seconds) -> height:
    return -4.7 * t**2 + 7.8 * t + 1.5


# 1 ---------------------------------------
# from typing import Callable


def dichotomy_method(func: Callable[[float], float],
                     a: float,
                     b: float,
                     epsilon: float) -> float:
    while True:
        x: float = (a + b) / 2
        y: float = func(x)

        if func(a) * y < 0:
            b = x
        else:
            a = x

        if abs(y) <= epsilon or abs(b - a) <= epsilon:
            return x


# 2 ---------------------------------------
# from typing import Callable


def approximate_derivative(func: Callable[[float], float],
                           x: float,
                           delta: float = .000001) -> float:
    return (func(x + delta) - func(x)) / delta


def newton_method(func: Callable[[float], float],
                  x: float,
                  epsilon: float) -> float:
    while True:
        x: float = x - func(x) / approximate_derivative(func, x)

        if abs(func(x)) <= epsilon:
            return x


# 3 ---------------------------------------
# from typing import Callable


def chords_method(func: Callable[[float], float],
                  a: float,
                  b: float,
                  epsilon: float) -> float:
    while True:
        x: float = a - ((func(a) * (b - a)) / (func(b) - func(a)))
        y: float = func(x)

        if func(a) * y < 0:
            b = x
        else:
            a = x

        if abs(y) <= epsilon or abs(b - a) <= epsilon:
            return x


if __name__ == '__main__':
    print(f'{dichotomy_method(h, 0, 3, 0.001)=}')
    # в методе Ньютона используется начальное приближение 3,
    # потому что при 0 будет искаться корень не а итервале [0, 3]
    print(f'{newton_method(h, 3, 0.001)=}')
    print(f'{chords_method(h, 0, 3, 0.001)=}')
