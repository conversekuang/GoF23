#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: converse
@version: 1.0.0
@file: singleton.py
@time: 2021/9/3 10:15
"""
import threading
import time


# 装饰器
def singleton():
    pass


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, ):
        time.sleep(0.3)

    @staticmethod
    def get_instance_static():
        if Singleton._instance is None:
            with Singleton._lock:
                if Singleton._instance is None:
                    Singleton._instance = Singleton()
        return Singleton._instance

    @classmethod
    def get_instance_class(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         with cls._lock:
    #             if cls._instance is None:
    #                 time.sleep(0.1)
    #                 cls._instance = super().__new__(cls)
    #     return cls._instance


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
