#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_argv.py
@Time   :   2021/5/28 13:49   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import os
import unittest


import sys
sys.argv=["1",2,4]
a = sys.argv[0:]
# print(a.pop())
print(a)
