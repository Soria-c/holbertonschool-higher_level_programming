#!/usr/bin/python3
"""
This module defines the functions:
    print_data()
"""
from sys import stdin
import signal


status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
               "403": 0, "404": 0, "405": 0, "500": 0}
count = 0
total_size = 0


def print_data(singal=None, frame=None):
    """Prints statistics data"""
    print(f"File size: {total_size}")
    for j, k in status_code.items():
        if (k):
            print(f"{j}: {k}")


signal.signal(signal.SIGINT, print_data)
for i in stdin:
    count += 1
    line = i.strip("\n").split(" ")
    total_size += int(line[-1])
    status_code[line[-2]] += 1
    if count == 10:
        print_data()
        count = 0
