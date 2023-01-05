#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
        upper += letter
    print("{}".format(upper))
