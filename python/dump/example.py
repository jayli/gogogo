#!/usr/bin/env python3
# debugger_entry = ../index.py
# -*- coding: utf-8 -*-

from dump.dump import dump
import time, sys

class A:       pass
class B(A):    pass
class C(A):    pass
class D(B, C): pass
class E:       pass
class F(D, E): pass

def init():
    print("---------------->>")
    dump('')
    dump(dump)
    dump(1)
    dump(1.1)
    dump(True)
    dump(None)
    dump((1,2,3,4))
    dump([1,2,3,4])
    dump({'a':1,'b':2,'c':{'d':3}})
    dump({'a','b','c','d'})
    dump(A)
    dump(F)
    dump(F())
    dump(F.__call__)
    print('--')
    see(1)
    dump(abs)
    dump(lambda x:x)
    dump((x for x in range(10)))
    dump(b'a')
    dump(time)
    dump(sys.implementation)
    dump(type.__dict__)
    print('end')
    return None

def see(p):
    li = []
    for a in dir(p):
        li.append({
            'name':a,
            'value':p.__getattribute__(a),
        })
    for b in li:
        print(b['name'], " => ", b['value'])
    return li
