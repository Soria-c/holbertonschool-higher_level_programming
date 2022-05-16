#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""
    if not(isinstance(my_list, list)):
        return 0
    x2 = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            x2 += 1
        print()
    except IndexError:
        print()
        return x2
    return x
