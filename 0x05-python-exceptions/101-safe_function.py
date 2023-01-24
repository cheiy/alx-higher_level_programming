#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(args)
    except (ValueError, IndexError) as err:
        print("Exception:", err)
        res = None
    return res
