#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

setup(
    name = "GOGOGO",
    py_modules = ["GOGOGO"],
    author = "jayli",
    author_email = "bachi@taobao.com",
    version = "0.1",
    packages = find_packages(exclude=('tests','docs')),
    install_requires = [],
)
