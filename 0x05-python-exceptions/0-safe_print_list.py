#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for item in my_list:
            if length < x:
                print("{:d}".format(item), end="")
                length += 1
        print()
    except TypeError:
        print("Type Error")
    return (length)
