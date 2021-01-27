# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:10
# @Author  : WardenAllen
# @File    : pluto_file_test.py
# @Brief   : 

# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 10:25
# @Author  : WardenAllen
# @File    : gui_test.py
# @Brief   :

import unittest
from .pluto_file import *

class TestFile(unittest.TestCase):
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
        path = 'C:/Projects/VS2019Projects/pluto/library/python/plutopy'
        # list_files(path)
        # list_folders(path, True, True)

        move_folder("C:/Users/admin/Desktop/test/2", "C:/Users/admin/Desktop/test/1")


    @unittest.skip("do't run as not ready")
    def test_with_skip(self):
        """Test method minus(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)