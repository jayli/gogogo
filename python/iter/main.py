#!/usr/bin/env python3
# debugger_entry = ../index.py

def init():
    """docstring for init"""
    print("---------------->>")
    print("sdfsfdsf")

    list = [1,2,3,4,5,6]
    it = iter(list)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break

    #----------fibonacci----------
    fibonacci(10)

    return None
    
def fibonacci(n):
    """docstring for fibonacci"""

    a , b , conter = 0 , 1  ,0
    fib_list = [0, 1]
    
    while conter <= n:
        if conter < 2:
            conter += 1
            continue
        else: pass
        fib_list.append(fib_list[conter - 2] + fib_list[conter - 1])
        conter += 1
    
    print(fib_list)

    return None
    
