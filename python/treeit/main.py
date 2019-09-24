#!/usr/bin/env python3
# debugger_entry = ../index.py

from dotmap import DotMap as DotMap

'''
dotmap_obj: {'F':{'D':{'B': 'object'}...}}
formated_obj: [{'name': 'F', 'child': [{'name': 'D', 'child': 'object'}]}]
printable_original_treelist: [[' ', 'F'], [' ', '├', 'D'], [' ', ' ', '├', 'B'],...]
printable_modified_treelist: [[' ', 'F'], [' ', '├', 'D'], [' ', '│', '├', 'B'],...]
'''

class TreeIt(object):
    
    dotmap_obj = DotMap({}) # 要打印的原始列表
    formated_obj = DotMap({}) # 转换格式后的原始列表
    printable_original_treelist = [] # 可以直接输出的修饰前的列表
    printable_modified_treelist = [] # 可以直接输出的修饰后的列表

    def __init__(this, dotmap_obj):
        """docstring for init"""
        if type(dotmap_obj) != DotMap:
            this.dotmap_obj = DotMap(dotmap_obj)
        else:
            this.dotmap_obj = dotmap_obj
        this.formated_obj = this.get_formated_treelist(this.dotmap_obj)
        this.printable_original_treelist = this.get_original_treelist(this.formated_obj)
        this.printable_modified_treelist = this.get_modified_treelist(0, this.printable_original_treelist)

    def get_formated_treelist(this, obj):
        all_list = []
        for item in dir(obj):
            child_var = obj[item]
            if type(child_var) == type(DotMap({})):
                child_node = this.get_formated_treelist(child_var)
            else:
                child_node = child_var
            parsed_obj = {
                "name":item,
                "child":child_node,
            }
            all_list.append(parsed_obj)
        return all_list 

    # 打印
    def print_tree(this):
        lop = this.printable_modified_treelist
        for line in lop:
            out_str = ''
            for item in line:
                out_str = out_str + item
            print(out_str)
        return None

    # 从结构化好的树形对象绘制 Tree
    def get_original_tree(this, printable_list, level, full_output):
        line_output = []

        index = 1
        if level == 1:
            # TODO printable_list.name 不存在
            line_output = [" ", printable_list[0]['name']]
            printable_list = printable_list[0]
        else:
            line_output = this.generate_placeholders(level)
            line_output.extend(["└", printable_list['name']])

        full_output.append(line_output)
        if type(printable_list['child']) == type([]):
            for supstrcture in printable_list['child']:
                this.get_original_tree(supstrcture, level + 1, full_output)
        else:
            end_line = this.generate_placeholders(level + 1)
            end_line.extend(["└", printable_list['child']])
            full_output.append(end_line)

        return full_output

    def generate_placeholders(this, No, placeholder = " "):
        index = 1
        tmp_line = []
        while index < No:
            tmp_line.append(placeholder)
            index += 1
        return tmp_line

    def get_original_treelist(this, obj):
        # Tree of obj
        return this.get_original_tree(obj, 1, [])


    # ---------------
    # line_number: 当前游标所在的行索引,0,1,2,3,4...
    # full_output: 当前可视结构的全量数组
    # return: 返回修正之后的全量数组
    def get_modified_treelist(this, line_number, full_output):
        # 当前数组长度, 1,2,3,4...
        current_length = len(full_output[line_number])

        # 如果遍历结束，直接返回全量数组，结束递归
        if line_number == len(full_output) - 1:
            return full_output

        # 找到当前行所属的根节点位置（0,1,2,3...）
        myroot = this.get_root_number(line_number,full_output)

        # 找到所属根节点后，修改连接线样式
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

        return this.get_modified_treelist(line_number + 1, full_output)

    # 得到当前行所属的根节点位置 return 0,1,2,3...
    def get_root_number(this, line_number, full_output):
        myroot = 0
        current_length = len(full_output[line_number])
        index = line_number - 1
        while index > 0:
            # 寻找根节点
            tmp = full_output[index]
            if len(tmp) == current_length - 1: # 找到根节点
                myroot = index
                break
            index -= 1
        return myroot
