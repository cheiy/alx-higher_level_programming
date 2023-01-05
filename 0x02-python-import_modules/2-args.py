#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv)
    if args == 1:
        print("argument:.")
    elif args == 2:
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    for i in range(args):
        if i != 0:
            print("{}: {}".format(i, sys.argv[i]))
