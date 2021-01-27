# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:18
# @Author  : WardenAllen
# @File    : time_test.py
# @Brief   : 

import unittest
import util.time as tm
import time

class TestConfig(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        """Test method add(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))

        print(tm.now_ns())
        print(tm.now_us())
        print(tm.now_ms())
        print(tm.now())
        print(tm.now_str())
        print(tm.now_ms_str())
        print(tm.today())
        print(tm.ts_from_str('2020-11-22 16:17:23'))
        print(tm.str_from_ts(1606033193))


    @unittest.skip("do't run as not ready")
    def test_with_skip(self):
        """Test method minus(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)