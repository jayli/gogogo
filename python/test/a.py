#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def resolve(num):
    i = 2
    while i <= num:
        if num % i == 0:
            print(i)
            resolve(num / i)
            break
        i = i + 1
        continue

if __name__ == "__main__":
    resolve(22)
