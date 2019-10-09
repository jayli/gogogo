#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# debugger_entry = ../index.py

from dotmap import DotMap as DotMap
from treeit import main as TreeitUtil
import sys, json

class A:       pass
class B(A):    pass
class C(A):    pass
class D(B, C): pass
class E:       pass
class F(D, E): pass

def init():

    klass_dotmap = parse_class_obj_to_dotmap(F)
    print('klass_dotmap')
    print(repr(klass_dotmap))
    print(json.dumps(klass_dotmap, sort_keys=True, indent=2))
    # klass_dotmap.pprint(pformat='json')

    print("---------------->>")

    o = TreeitUtil.TreeIt(klass_dotmap)
    o.print_tree()

def parse_class_obj_to_dotmap(klass):
    root_obj = {}
    try:
        root_obj[klass.__name__] = create_object_from_class(klass)
        return root_obj
        # return DotMap(root_obj)
    except AttributeError:
        print('入参应该是类', sys.exc_info()[0])
    return None

def create_object_from_class(klass):
    # 如果是根类
    if type(klass) is not type:
        return klass

    if klass.__base__ is object:
        return 'object'

    # new_obj = DotMap()
    new_obj = {}
    for item in klass.__bases__:
        if type(item) is not type:
            new_obj[str(item)] = " "
        else:
            new_obj[item.__name__] = create_object_from_class(item)
    return new_obj

