#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   :   my_test_class_p.py 
@Time   :   2021/6/16 18:12   
@Contact    :      
@Author     :   WG
@Version    :   v 0.1
@Desc   :   
"""
import pytest

from seleniumbase import BaseCase


class MytestClass_P(BaseCase):
    def __init__(self):
        super(MytestClass_P, self).__init__()

    def setUp(self):
        super(MytestClass_P, self).setUp()

    @pytest.fixture(scope='class', autouse=True)
    def set_driver(self):
        print("set")