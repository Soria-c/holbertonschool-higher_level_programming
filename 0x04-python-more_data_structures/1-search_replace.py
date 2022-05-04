#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new with search replaced by replaced in my_list"""
    if not isinstance(my_list, list):
        return
    return [i if i != search else replace for i in my_list]
