#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        val = a_dictionary.get(key) * 2
        new_dict.update({key: val})
    return (new_dict)
