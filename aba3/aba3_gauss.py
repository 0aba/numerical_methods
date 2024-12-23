from typing import Union

type number = Union[int, float]
type matrix = tuple[list[number],
                    ...
                    ]
type result_SLAE = list[number]


def gauss_method(mat: matrix) -> result_SLAE:
    result: result_SLAE = [0] * len(mat)
    len_column: int = len(mat)
    len_row: int = len(mat[0])

    for k in range(len_column):
        for j in range(len_row - 1, -1, -1):
            mat[k][j] /= mat[k][k]

        # info! "if k < size_y" не имеет смылса в python
        for i in range(k + 1, len_column):
            for j in range(len_row - 1, k - 1, -1):
                mat[i][j] -= mat[i][k] * mat[k][j]

    for y in range(len_column - 1, -1, -1):
        result[y] = mat[y][len_row - 1]
        for x in range(len_row - 2, y, -1):
            result[y] -= mat[y][x] * result[x]

    return result
# -----------------------------------------------


if __name__ == '__main__':
    import pprint

    input_matrix: matrix = ([4, 1, 4, 32],
                            [3, 1, 5, 29],
                            [2, 1, 5, 24])

    print('Матрица до Гаусса:')
    pprint.pprint(input_matrix, width=40)

    result_gauss: result_SLAE = gauss_method(input_matrix)

    print('Матрица после Гаусса:')
    pprint.pprint(input_matrix, width=40)

    print('Результат метода Гаусса:')
    pprint.pprint(result_gauss, width=40)
