#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    str_len = len(str)
    for i in range(str_len):
        if i != n:
            str2 += str[i]
    return (str2)
