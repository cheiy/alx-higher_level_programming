#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    type_ = type(roman_string)
    if type_ is None:
        return (0)
    dict_ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for letter in roman_string:
        num += dict_ro.get(letter)
    return (num)
