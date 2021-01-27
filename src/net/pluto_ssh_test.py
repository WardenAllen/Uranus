# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 14:54
# @Author  : WardenAllen
# @File    : pluto_ssh_test.py
# @Brief   : 

import unittest
from .pluto_ssh import *

class TestSSH(unittest.TestCase):
    """Test mathfuc.py"""

    __data = dict()

    @classmethod
    def setUpClass(cls):
        print ("this setupclass() method only called once.\n")

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

        ssh = PlutoSSH()
        ssh.connect_by_pass('192.168.1.24', 22, 'root', 'wangdong')
        ssh.execute('ls -a')

    @unittest.skip("do't run as not ready")
    def test_with_skip(self):
        """Test method minus(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)