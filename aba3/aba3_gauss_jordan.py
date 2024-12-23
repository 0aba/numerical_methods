from typing import Union

type number = Union[int, float]
type matrix = tuple[list[number],
                    ...
                    ]
type result_SLAE = list[number]


def gauss_jordan_method(mat: matrix) -> result_SLAE:
    size_y: int = len(mat)
    size_x: int = len(mat[0])

    for k in range(size_y):
        for j in range(size_x - 1, -1, -1):
            mat[k][j] /= mat[k][k]

        # info! "if k < size_y" не имеет смылса в python
        for i in range(k + 1, size_y):
            for j in range(size_x - 1, k - 1, -1):
                mat[i][j] -= mat[i][k] * mat[k][j]

    for y in range(size_y - 1, -1, -1):
        for x in range(size_x - 1 - 1, 0 + y, -1):
            mat[y][size_x - 1] -= mat[y][x] * mat[x][size_x - 1]
            mat[y][x] = 0

    return [mat[y][size_x - 1] for y in range(size_y)]
# -----------------------------------------------


if __name__ == '__main__':
    import pprint
    input_matrix: matrix = ([4, 1, 4, 32],
                            [3, 1, 5, 29],
                            [2, 1, 5, 24])

    print('Матрица до Гаусса-Жордана:')
    pprint.pprint(input_matrix, width=40)

    result_gauss: result_SLAE = gauss_jordan_method(input_matrix)

    print('Матрица после Гаусса-Жордана:')
    pprint.pprint(input_matrix, width=40)

    print('Результат метода Гаусса-Жордана:')
    pprint.pprint(result_gauss, width=40)
