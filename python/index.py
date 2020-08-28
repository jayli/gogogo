#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inherit.all as InheritExample
import iter.main as IterExample
import decorator.main as DecoratorExample
import treeit.tree as Tree
# import web.main as WebExample
import dump.example as DumpExample

import guiexp.main as GUIexp

if __name__ == "__main__":
    InheritExample.init()
    IterExample.init()
    #WebExample.init()
    DecoratorExample.init()
    Tree.init()
    DumpExample.init()
    GUIexp.entry()

    print('================================')

