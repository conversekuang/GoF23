#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: closure.py
@time: 2021/9/9 14:04
"""


def closure():
    greetings = "hey"
    def wapper(name):
        print(greetings, name)
    return wapper




if __name__ == '__main__':
    f = closure()
    f("kzk")