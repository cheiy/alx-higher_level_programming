#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []

    def multiply(list_item):
        res = list_item * number
        return (res)
    new_list = list(map(multiply, my_list))
    return (new_list)
