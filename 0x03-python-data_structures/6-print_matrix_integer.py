#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
    else:
        for list in matrix:
            list_len = len(list)
            count = 1
            for item in list:
                if count < list_len:
                    print("{:d}".format(item), end=" ")
                else:
                    print("{:d}".format(item))
                count += 1
