#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if ((idx < 0) or (idx > len(my_list) - 1)):
        return [i for i in my_list]
    return [i if my_list.index(i) != idx else element for i in my_list]
