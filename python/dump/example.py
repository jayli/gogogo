#!/usr/bin/env python3
# debugger_entry = ../index.py
# -*- coding: utf-8 -*-

#from dump.dump import dump
import time, sys
import json

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
    print('--')
    dump(F())
    dump(F.__call__)
    print('--')
    #see(1)
    dump(abs)
    dump(lambda x:x)
    dump((x for x in range(10)))
    dump(b'a')
    dump(time)
    dump(sys.implementation)
    dump(type.__dict__)
    dump([].append)
    dump(object.__init__)
    dump(object().__str__)
    dump(str.join)
    dump(dict.__dict__['fromkeys'])
    dump(sys)
    dump(type(dump).__code__)
    dump(type(dump).__globals__)

    dump(_cell_factory())
    async def _c(): pass
    _c = _c()
    dump(_c)
    _c.close()

    async def _ag():
        yield
    _ag = _ag()
    dump(_ag)

    print('end')
    return None


def _cell_factory():
    a = 1
    def f():
        nonlocal a
    return f.__closure__[0]

def dump(p):
    print(type(p))


def see(p):
    li = []
    li_dump = {}
    for a in dir(p):
        li.append({
            'name':a,
            'value':p.__getattribute__(a),
        })
        li_dump[a] = str(p.__getattribute__(a))
    # for b in li:
    #     print(b['name'], " => ", b['value'])
    print(json.dumps(li_dump, sort_keys=True, indent=2))
    return li
