#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for lis in matrix:
        temp_list = []
        for item in lis:
            square_item = item * item
            temp_list.append(square_item)
        new_list.append(temp_list)
    return (new_list)
