#!/usr/bin/python3
def print_last_digit(number):
    num_string = str(number)
    last_digit = num_string[-1]
    real_num = int(last_digit)
    print("{}".format(real_num), end="")
    return(last_digit)
