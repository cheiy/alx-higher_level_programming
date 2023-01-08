#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)
    high = list_len - 1
    while high >= 0:
        print("{:d}".format(my_list[high]))
        high -= 1
