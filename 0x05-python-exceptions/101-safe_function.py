#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(args)
    except Exception as err:
        print("Exception: {}".format(type(err)), file=sys.stderr)
        raise
        res = None
    return res
