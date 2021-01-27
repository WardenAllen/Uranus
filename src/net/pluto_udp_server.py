# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:58
# @Author  : WardenAllen
# @File    : pluto_udp_server.py
# @Brief   : 

from socket import *
from . import pluto_net as net

class PlutoUdpServer(net.PlutoNet):

    def __init__(self, host_, port_):
        super(PlutoUdpServer, self).__init__(host_, port_, AF_INET, SOCK_DGRAM)

    def bind(self):
        return self._socket.bind(self._address)

    def send(self, data_, addr_):
        return self._socket.sendto(data_.encode('utf-8'), addr_)

    def recv(self):
        return self._socket.recvfrom(self._MAX_BUFF_SIZE)