#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_Memory.py 
@Time   :   2021/6/5 15:17   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
# import sys
#
#
# class test_memory():
#     def test1(self):
#         pass
# if __name__ == '__main__':
#     print(sys.getrefcount(test_memory))


# def f1():
#     for i in range(5):
#         def n():
#             print(i)
#     return n
#
#
# print(f1().__repr__())
import sys


def f1(n):
    print("in function:", sys.getrefcount(n) - 1)


x = 22
print("init x：", sys.getrefcount(x) - 1)
a = 22
print("after a：", sys.getrefcount(x) - 1)
b = a
print("after b：", sys.getrefcount(x) - 1)
f1(x)
print("after function：", sys.getrefcount(22) - 1)