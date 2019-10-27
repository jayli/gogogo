#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_log():
    print("ok")

def foo(a=""):
    __import__('pdb').set_trace()
    pass

def main():
    print_log()
    foo()

if __name__ == '__main__':
    main()
