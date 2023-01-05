#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    args = len(sys.argv)
    if args == 1:
        sum = 0
    else:
        for i in range(args):
            if i != 0:
                sum += int(sys.argv[i])
    print("{}".format(sum))
