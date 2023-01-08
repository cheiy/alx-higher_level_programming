#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    else:
        for list in matrix:
            list_len = len(list)
            count = 1
            for item in list:
                if count < list_len:
                    print("{}".format(item), end=" ")
                else:
                    print("{}".format(item))
                count += 1
