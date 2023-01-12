#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = []
    for key_ in a_dictionary:
        keys.append(key_)
    if key not in keys:
        return (a_dictionary)
    else:
        a_dictionary.pop(key)
    return (a_dictionary)
