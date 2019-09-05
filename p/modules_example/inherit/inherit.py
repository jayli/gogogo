#!/usr/bin/env python3

class A:       pass
class B(A):    pass
class C(A):    pass
class D(B, C): pass
class E:       pass
class F(D, E): pass

def init():
    print('ok')
    b = B()
    print(dir(type(F())))

    objecttree(F())

def classtree(cls, indent):
    print("." * indent + cls.__name__)
    for supcls in cls.__bases__:
        classtree(supcls, indent + 3)

def objecttree(obj):
    print("Tree of", obj)
    classtree(obj.__class__, 3)



