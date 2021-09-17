#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

try:    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

reqs = parse_requirements("requirements.txt", session = False)

setup (
    name             = "GOGOGO",
    py_modules       = ["GOGOGO"],
    author           = "jayli",
    author_email     = "bachi@taobao.com",
    version          = "0.1",
    packages         = find_packages(exclude=('tests','docs')),
    install_requires = [str(ir.req) for ir in reqs],
)
