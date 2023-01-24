#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        i = 0
        while i < list_length:
            try:
                res = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("{}".format("division by 0"))
                res = 0
            except IndexError:
                print("{}".format("out of range"))
                res = 0
            except TypeError:
                print("{}".format("wrong type"))
                res = 0
            finally:
                new_list.append(res)
                i += 1
    finally:
        return new_list
