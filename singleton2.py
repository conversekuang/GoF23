#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: singleton2.py
@time: 2021/9/3 15:25
"""
# 函数实现装饰器，来修饰单例的类。


import threading
import time


def singleton(cls):
    _instance = {}
    _lock = threading.Lock()

    def _inner():
        if cls not in _instance:
            with _lock:
                if cls not in _instance:
                    time.sleep(0.2)
                    _instance[cls] = cls()
        return _instance[cls]
    return _inner

@singleton
class Singleton:
    pass


def multi_thread(i):
    obj = Singleton()
    # obj = Singleton.get_instance_static()
    # obj = Singleton.get_instance_class()
    print(obj, i)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=multi_thread, args=[i, ])
        t.start()
