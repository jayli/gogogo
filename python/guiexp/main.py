#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course
# debugger_entry = ../index.py

import tkinter as tk

def entry():
    """docstring for entry"""
    print('hello world')

    root = Root()
    root.mainloop()

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lable = tk.Label(self, text="-----------------hello----------------")
        self.lable.pack()
