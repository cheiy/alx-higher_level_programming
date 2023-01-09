#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 1 and len(tuple_b) > 1:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        if len(tuple_a) > 1:
            val1_a = tuple_a[0]
            val2_a = tuple_a[1]
            if len(tuple_b) == 0:
                val1_b = 0
                val2_b = 0
            if len(tuple_b) == 1:
                val1_b = tuple_b[0]
                val2_b = 0
        if len(tuple_b) > 1:
            val1_b = tuple_b[0]
            val2_b = tuple_b[1]
            if len(tuple_a) == 0:
                val1_a = 0
                val2_a = 0
            if len(tuple_a) == 1:
                val1_a = tuple_a[0]
                val2_a = 0
        if len(tuple_a) == 0:
            val1_a = 0
            val2_a = 0
        if len(tuple_b) == 0:
            val1_b = 0
            val2_b = 0
        if len(tuple_a) == 1:
            val1_a = tuple_a[0]
            val2_a = 0
        if len(tuple_b) == 1:
            val1_b = tuple_b[0]
            val2_b = 0
        tuple_c = (val1_a + val1_b, val2_a + val2_b)
    return (tuple_c)
