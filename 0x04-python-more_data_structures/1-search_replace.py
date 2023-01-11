#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new_list = []
    replace_item_count = my_list.count(search)
    for item in my_list:
        new_list.append(my_list[i])
        i += 1
    i = 0
    for item in my_list:
        if item == search:
            new_list[i] = replace
        i += 1
    return (new_list)
