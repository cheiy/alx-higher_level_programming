#!/usr/bin/python3
x = 2
upper = 90
lower = 122
i = 1
while i <= 26:
    if ((x % 2) == 0):
        print("{}".format(chr(lower)), end="")
        lower -= 1
        upper -= 1
    else:
        print("{}".format(chr(upper)), end="")
        upper -= 1
        lower -= 1
    x += 1
    i += 1
