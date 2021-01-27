# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 15:51
# @Author  : WardenAllen
# @File    : pluto_udp_test.py
# @Brief   : 

import unittest
import time
import net.pluto_udp_client as uc
import net.pluto_udp_server as us

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

    def test_server(self):
        """Test method add(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))

        server = us.PlutoUdpServer('0.0.0.0', 8888)
        server.bind()

        while True:
            print("waiting for message...")
            data, addr = server.recv()
            print("recv : ", data.decode('utf-8'))
            server.send('hello from server 测试中文.', addr)

    def test_client(self):

        client = uc.PlutoUdpClient('192.168.1.23', 8888)

        while True:
            log = 'hello from client 测试中文.'
            log_bytes = log.encode('utf-8')

            lt = 1
            lt_bytes = lt.to_bytes(length=1, byteorder='big', signed=False)

            ts = int(time.time() * 1000)
            ts_bytes = ts.to_bytes(length=8, byteorder='big', signed=True)

            data = lt_bytes + ts_bytes + log_bytes

            client.raw_send(data)
            # data, addr = client.recv()
            # print("recv : ", data.decode('utf-8'))
            time.sleep(1)


    @unittest.skip("do't run as not ready")
    def test_with_skip(self):
        """Test method minus(a, b)"""
        # self.assertEqual(3, add(1, 2))
        # self.assertNotEqual(3, add(2, 2))


if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)