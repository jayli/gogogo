#!/usr/bin/env python3
# debugger_entry = ../index.py

#from turtle import * 

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

    #----------fibonacci---------- {{{
    fibonacci(10)

    #---------------------------- }}}
    test1()

    # 图形编程
    # test_turtle()

    return None

def test1():
    """docstring for test1"""
    info = [1,2,3,4,5,6,7,8]
    print(list(range(1,11)))

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

def test_turtle():
    def drawStar(x, y):
        pu()
        goto(x, y)
        pd()
        # set heading: 0
        seth(0)
        for i in range(5):
            fd(40)
            rt(144)

    for x in range(0, 250, 50):
        drawStar(x, 0)

    done()

    return None

