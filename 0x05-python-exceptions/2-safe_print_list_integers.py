#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    real_length = 0
    for item in my_list:
        try:
            while x > 0:
                print("{:d}".format(my_list[length]), end="")
                length += 1
                real_length += 1
                x -= 1
        except (TypeError, ValueError):
            length += 1
            x -= 1
    print()
    return (real_length)
