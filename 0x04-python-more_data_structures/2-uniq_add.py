#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = dups_sum = uniq_sum = 0
    uniq = lambda item: my_list.count(item) == 1
    unique = list(filter(uniq, my_list))
    dup = lambda item: my_list.count(item) > 1
    dups = list(filter(dup, my_list))
    for item in dups:
        dups_sum += item
    for item in unique:
        uniq_sum += item
    result = (int(dups_sum / 2) + uniq_sum)
    return (result)
