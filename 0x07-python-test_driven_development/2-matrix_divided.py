#!/usr/bin/python3
""" Module contains the matrix_divided function """


def matrix_divided(matrix, div):
    """ Function divides all elements of a matrix """

    try:
        error_1 = 'matrix must be a matrix (list of lists) of integers/floats'
        error_2 = 'Each row of the matrix must have the same size'
        new_matrix = []
        for item in matrix:
            for sub_item in item:
                if isinstance(sub_item, (int, float)) is False:
                    raise TypeError(error_1)
        item_len = len(matrix[1])
        for item in matrix:
            current_len = len(item)
            if current_len != item_len:
                raise TypeError(error_2)
        if isinstance(div, (float, int)) is False:
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')
        for item in matrix:
            new_list = []
            for sub_item in item:
                res = sub_item / div
                new_list.append(round(res, 2))
            new_matrix.append(new_list)
        return new_matrix
    except TypeError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
