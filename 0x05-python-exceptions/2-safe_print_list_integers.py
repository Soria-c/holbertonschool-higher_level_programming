#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints x elements of a list and only integers"""
    x2 = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            x2 += 1
        except (TypeError, ValueError):
            continue
    print()
    return x2
