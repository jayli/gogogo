#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dotmap import DotMap as CreateObject
import re

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
    print("---------------->>")

    full_output = trim_tree_list(modify_node(0,full_output))
    show_the_tree(full_output)


def trim_tree_list(full_output):
    for arr in full_output:
        if re.match(r"^\s*$",arr[0]):
            arr.pop(0)
    return full_output

def show_the_tree(full_output):
    for item in full_output:
        print("".join(item))
    return full_output

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

# line_number: 当前游标所在的行索引,0,1,2,3,4...
# full_output: 当前可视结构的全量数组
# return: 返回修正之后的全量数组
def modify_node(line_number, full_output):
    # 当前数组长度, 1,2,3,4...
    current_length = len(full_output[line_number])

    # 如果遍历结束，直接返回全量数组，结束递归
    if line_number == len(full_output) - 1:
        return full_output

    # 找到当前行所属的根节点位置（0,1,2,3...）
    myroot = 0
    index = 0
    while index < line_number:
        # 寻找根节点
        tmp = full_output[index]
        if len(tmp) == current_length - 1: # 找到根节点
            myroot = index
            break
        index += 1
    # print("root_node", myroot)

    # 找到所属根节点后，修改连接线样式
    # TODO 这里有问题
    tdex = myroot + 1
    while tdex < line_number:
        tmp = full_output[tdex]
        if len(tmp) == current_length:
            if len(full_output[tdex + 1]) > len(tmp):
                tmp[current_length - 2] = "├"
            else: pass
        elif len(tmp) > current_length:
            tmp[current_length - 2] = "│"
        else: pass
        tdex += 1

    return modify_node(line_number + 1, full_output)

    
