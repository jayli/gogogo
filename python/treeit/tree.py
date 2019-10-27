#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# debugger_entry = ../index.py

import os

def init():
    print("---------------->> Tree")
    print(os.getcwd())
    print(os.listdir())
    list_dir = get_listdir(os.getcwd())
    pass

def get_listdir(path="."):
    """
    {
        "direc":["a","b","c"],
        "files":["d","e","f"]
    }
    """
    list_dir = {
        "directories":[],
        "files":[]
    }

    a = os.scandir(path)
    __import__('pdb').set_trace()
    pass

    # for item in os.listdir(path):

    return None


