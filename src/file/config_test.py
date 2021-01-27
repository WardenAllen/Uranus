# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 15:14
# @Author  : WardenAllen
# @File    : config_test.py
# @Brief   : 

import unittest
import file.excel as excel
import file.config as config

class TestConfig(unittest.TestCase):
    """Test mathfuc.py"""

    __data = dict()

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")
        e = excel.Excel()
        e.open('./data/config/test.xlsx')
        cls.__data = e.read()

    @classmethod
    def tearDownClass(cls):
        print ("this teardownclass() method only called once too.\n")

    def setUp(self):
        print ("do something before test : prepare environment.\n")

    def tearDown(self):
        print ("do something after test : clean up.\n")

    def test(self):
        """Test method add(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))

        obj = dict()
        obj['ServerList'] = dict()
        obj['ServerList']['List'] = self.__data

        config.write_json(obj, './data/config/test.json')
        config.write_toml(obj, './data/config/test.toml')

        print(config.read_json('./data/config/test.json'))
        print(config.read_toml('./data/config/test.toml'))

    @unittest.skip("do't run as not ready")
    def test_with_skip(self):
        """Test method minus(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)