#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   test_settings.py
@Time   :   2021/5/31 17:55
@Contact    :
@Author     :   WG
@Version    :   v 0.1
@Desc   :

"""
from seleniumbase import config as sb_config

wg = "wg"
class test_sb():
    wg3 = None

    def __init__(self):
        self.wg2 = "234"
        self.wg = "test.wg"

    def wg1(self):
        global wg4
        wg4 = self.wg
        wg3 = wg
        print(wg4,wg3)
        print(wg,self.wg)

    def wg_notused(self):
        self.wg5 = None

    @classmethod
    def wg_classmate(cls):
        cls.wg6 = "None"


if __name__ == '__main__':
    ts = test_sb()
    # ts.wg1()
    var1 = ts.wg
    print("类的属性")
    print("定义类（test_sb） hasattr wg（实例变量）:", hasattr(test_sb, "wg"))
    print("定义类（test_sb） hasattr wg1(方法):", hasattr(test_sb, "wg1"))
    print("定义类（test_sb） hasattr wg2（实例变量）:", hasattr(test_sb, "wg2"))
    print("定义类（test_sb） hasattr wg3（方法的局部变量）:", hasattr(test_sb, "wg3"))
    print("定义类（test_sb） hasattr wg4（定义的全局变量）:", hasattr(test_sb, "wg4"))
    print("定义类（test_sb） hasattr wg5（实例变量,未调用）:", hasattr(test_sb, "wg5"))
    print("定义类（test_sb） hasattr wg5（实例变量,未调用）:", hasattr(test_sb, "wg6"))
    print("实例（ts) hasattr wg:", hasattr(ts, "wg"))
    print("实例（ts) hasattr wg1:", hasattr(ts, "wg1"))
    print("实例（ts) hasattr wg2:", hasattr(ts, "wg2"))
    print("实例（ts) hasattr wg3:", hasattr(ts, "wg3"))
    print("实例（ts) hasattr wg4:", hasattr(ts, "wg4"))
    print("实例（ts) hasattr wg5:", hasattr(ts, "wg5"))
    print("实例（ts) hasattr wg5:", hasattr(ts, "wg6"))
    print(dir(test_sb))
    print(dir(ts))
