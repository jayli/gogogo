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

    print("----------------")

    full_output = object_tree(F())
    print(full_output)
    print("---------------->>")
    print(modify_node(0, full_output))


def class_tree(cls, level , full_output):
    line_output = []
    
    index = 1
    if level <= 1:
        line_output = [" ",cls.__name__]
    else:
        while index < level:
            line_output.append(" ")
            index += 1
        line_output.extend(["└", cls.__name__])
    
    full_output.append(line_output)
    # print(" " * level, "└─", cls.__name__)
    for supcls in cls.__bases__:
        class_tree(supcls, level + 1, full_output)

    return full_output

def object_tree(obj):
    print("Tree of", obj)
    return class_tree(obj.__class__, 1, [])

# 0,1,2,3...
def modify_node(line_number, full_output):
    node_level = len(full_output[line_number])
    print(full_output[line_number])

    if line_number == len(full_output) - 1:
        return full_output

    myroot = 0
    index = 0
    while index < line_number:
        # 寻找根节点
        tmp = full_output[index]
        if len(tmp) == node_level - 1: # 找到根节点
            myroot = index
            break
        index += 1

    # TODO 这里有问题
    tdex = myroot + 1
    while tdex < line_number:
        tmp = full_output[tdex]
        if len(tmp) == node_level:
            tmp[node_level - 2] = "├"
        else:
            tmp[node_level - 2] = "|"
        print(tmp)
        tdex += 1

    return modify_node(line_number + 1, full_output)

    
