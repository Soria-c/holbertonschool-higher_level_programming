#!/usr/bin/python3
def roman_to_int(roman_string):
    """Returns roman_string in decimal"""
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    r_s = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = 0
    for i in range(len(roman_string)):
        if (i > 0) and (r_s[roman_string[i]] > r_s[roman_string[i - 1]]):
            s += r_s[roman_string[i]] - r_s[roman_string[i - 1]] * 2
            continue
        s += r_s[roman_string[i]]
    return s
