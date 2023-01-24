#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except TypeError:
        pass
    except ZeroDivisionError:
        print("{}".format("Inside result: None"))
        result = None
    finally:
        try:
            print("{} {:.1f}".format("Inside result: ", result))
        except TypeError:
            pass
        return result
