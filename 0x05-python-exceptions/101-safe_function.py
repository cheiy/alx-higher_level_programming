#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(args)
    except Exception as err:
        print("Exception:", err)
        res = None
        raise
    return res
