#!/usr/bin/python3
def roman_to_int(roman_string):
    type_ = type(roman_string)
    if 'str' not in type_ and type_ is not None:
        return (0)
