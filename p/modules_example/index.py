#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath("./module1")) 

import ma
# from MyClass import TestClass
from module2.MyClass import TestClass
import inherit.inherit

#--------------------

def test_case_demo():
    """docstring for test_case_demo"""

    print(__name__)
    ma.say()
    print(sys.path)
    print(dir(ma))
    print("----------------------")
    

def sum_demo():
    """docstring for sum_demo"""
    return
    a = input('a:')
    b = input('b:')
    sum = int(a) + int(b)
    print('{0} + {1} = {2}'. format(a,b, sum))

if __name__ == "__main__":
    test_case_demo()
    # sum_demo()
    x = TestClass()
    print(x.foo())
    print(TestClass.__dict__)
    print("#---------------------")
    inherit.inherit.init()

    
