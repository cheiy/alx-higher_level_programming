#!/usr/bin/python3
def weight_average(my_list=[]):
    tup_sum = 0
    weight_sum = 0
    weighted_average = 0

    if len(my_list) == 0:
        return (0)
    for tup in my_list:
        tup_sum += (tup[0] * tup[1])
    for tup in my_list:
        weight_sum += tup[1]
    weighted_average = tup_sum / weight_sum

    return (weighted_average)
