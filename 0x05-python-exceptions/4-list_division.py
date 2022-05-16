#!/usr/bin/python3
from ast import Index


def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of two lists"""
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            result.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
