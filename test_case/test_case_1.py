#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/7/30 12:19
# @Author  : v_shxliu
# @File    : test_case_1.py
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.number = input('Enter a number:')
        self.number = int(self.number)

    def test_case_1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg='Your input is not 10')

    def test_case_2(self):
        print(self.number)
        self.assertEqual(self.number, 20, msg='Your input is not 20')

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg='Your input is not 30')

    def tearDown(self):
        print('Test over')
