# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:57
# @Author  : WardenAllen
# @File    : pluto_udp_client.py
# @Brief   : 

from socket import *
from . import pluto_net as net

class PlutoUdpClient(net.PlutoNet):

    def __init__(self, host_, port_):
        super(PlutoUdpClient, self).__init__(host_, port_, AF_INET, SOCK_DGRAM)

    def send(self, data_, addr_=''):
        return self._socket.sendto(data_.encode('utf-8'), self._address)

    def raw_send(self, bytes_):
        return self._socket.sendto(bytes_, self._address)

    def recv(self):
        return self._socket.recvfrom(self._MAX_BUFF_SIZE)