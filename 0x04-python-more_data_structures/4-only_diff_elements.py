#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    diff_1 = {item for item in set_1 if item not in set_2}
    diff_2 = {item for item in set_2 if item not in set_1}
    set_3 = set_3.union(diff_1, diff_2)
    return (set_3)
