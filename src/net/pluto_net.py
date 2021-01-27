# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 15:29
# @Author  : WardenAllen
# @File    : pluto_net.py
# @Brief   : 

import socket

class PlutoNet:

    _MAX_BUFF_SIZE = 65536

    _host = ''
    _port = 1437
    _socket = None
    _address = ()

    def __init__(self, host_, port_, family_=-1, type_=-1):
        self._socket = socket.socket(family_, type_)
        self._host = host_
        self._port = port_
        self._address = (host_, port_)

    def send(self, data_, addr_):
        pass

    def recv(self):
        pass

    def close(self):
        return self._socket.close()
