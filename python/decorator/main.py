#!/usr/bin/env python3
# debugger_entry = ../index.py

def init():
    """docstring for init"""
    print("sdfsdfdsfdsf")
    print(lazy_sum(1,2,3,4,5))
    return None


def lazy_sum(*args):
    """docstring for sum"""
    sum = 0
    for n in args:
        sum += n
    return sum

