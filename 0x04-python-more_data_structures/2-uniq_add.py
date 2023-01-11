#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = dups_sum = uniq_sum = 0
    if my_list is None:
        exit()
    for item in my_list:
        if my_list.count(item) > 1:
            dups_sum += item
        else:
            uniq_sum += item
    result = (int(dups_sum / 2) + uniq_sum)
    return (result)
