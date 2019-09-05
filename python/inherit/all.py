#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dotmap import DotMap as CreateObject

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

    object_tree(F())

    print("----------------")

    o = CreateObject({
        'a':1,
        'b':2,
        'c':{
            'd':3,
            'f':{
                'e':4
            }
        }
    })

    o.c.g = 5

    print(F.__bases__)

# def parse_classes_to_object(klass):
#     klass_obj = {'name':klass.__name__, 'super_classes':{}}
#     for super_classes in klass.__bases__:
#         klass_obj = 


def class_tree(cls, indent):
    print(" " * indent , "└─", cls.__name__)
    for supcls in cls.__bases__:
        class_tree(supcls, indent + 3)

def object_tree(obj):
    print("Tree of", obj)
    class_tree(obj.__class__, 3)



