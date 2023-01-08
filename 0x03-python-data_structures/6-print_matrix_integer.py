#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        list_len = len(list)
        count = 1
        for item in list:
            if count < list_len:
                print(item, end=" ")
            else:
                print(item)
            count += 1
