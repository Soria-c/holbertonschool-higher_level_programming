#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new, t1, t2 = (), tuple_a, tuple_b
    if not len(tuple_a):
        t1 = (0, 0)
    if len(tuple_a) == 1:
        t1 = (tuple_a[0], 0)
    if not len(tuple_b):
        t2 = (0, 0)
    if len(tuple_b) == 1:
        t2 = (tuple_b[0], 0)
    for i in range(0, 2):
        new = (*new, (t1[i] + t2[i]))
    return (new)
