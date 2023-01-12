#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def s_matrix(x):
        res = x * x
        return (res)
    result = []
    for list_ in matrix:
        result.append(list(map(s_matrix, list_)))
    return (result)
