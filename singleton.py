#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: singleton.py
@time: 2021/9/3 15:00
"""
import threading


class Singleton:
    _lock = threading.Lock()

    @classmethod
    def get_instance_class(cls):
        if not hasattr(Singleton, "_instance"):
            with Singleton._lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = cls()
        return Singleton._instance

    @staticmethod
    def get_instance_static():
        if not hasattr(Singleton, "_instance"):
            with Singleton._lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton()
        return Singleton._instance


def multi_thread(i):
    # obj = Singleton()
    obj = Singleton.get_instance_static()
    # obj = Singleton.get_instance_class()
    print(obj, i)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=multi_thread, args=[i, ])
        t.start()

    print(Singleton.__mro__)