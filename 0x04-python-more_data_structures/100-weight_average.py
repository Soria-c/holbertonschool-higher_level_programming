#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns a weighted average"""
    if not isinstance(my_list, list):
        return
    s1 = 0
    s2 = 0
    for i in my_list:
        s1 += i[1]
    for i in my_list:
        s2 += (i[0] * i[1]) / s1
    return s2
