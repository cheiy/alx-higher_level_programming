#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(args)
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        res = None
        raise
    return res
