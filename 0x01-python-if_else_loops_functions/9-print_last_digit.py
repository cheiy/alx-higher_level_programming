#!/usr/bin/python3
def print_last_digit(number):
    num_string = str(number)
    last_digit = num_string[-1]
    print("{}".format(last_digit), end="")
    return(last_digit)
