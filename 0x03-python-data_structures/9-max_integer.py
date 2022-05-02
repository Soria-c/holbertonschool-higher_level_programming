#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    m = my_list[0]
    for i in range(0, len(my_list) - 1):
        if (m < my_list[i + 1]):
            m = my_list[i + 1]
    return m
