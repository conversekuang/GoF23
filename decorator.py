#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: decorator.py
@time: 2021/9/9 13:47
"""

from functools import wraps


def decorator(f):
    @wraps(f)
    def inner_wapper():
        print(f.__name__)
        f()
    return inner_wapper


@decorator
def try_me():
    print("hi")


if __name__ == '__main__':
    print(try_me.__name__)