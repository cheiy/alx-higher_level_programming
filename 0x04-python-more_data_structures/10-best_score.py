#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0
    biggest_key = ""
    num = 0
    if a_dictionary is None:
        return (None)
    for key in a_dictionary:
        num = a_dictionary.get(key)
        if num > biggest:
            biggest = num
            biggest_key = key
    if a_dictionary.get(biggest_key) is None:
        return (None)
    return (biggest_key)
