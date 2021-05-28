#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_dots.py 
@Time   :   2021/5/28 15:47   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
# string = "'\\'1'23'4"
# print(string.count("'"))
# print(string.count("\\'"))
# if string.count("'") != string.count("\\'"):
#     string = string.replace("'", "\\'")
# if string.count('"') != string.count('\\"'):
#     string = string.replace('"', '\\"')
# print(string.count("'"))
# print(string.count("\\'"))
# print(string)
import os

paths = os.environ["PATH"].split(";")
print(paths)
