# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 12:02
# @Author  : WardenAllen
# @File    : pluto_ftp.py
# @Brief   : 

import paramiko

class PlutoFtp :

    # paramiko's Sftp() object.
    __sftp = object

    def connect_by_pass(self, host, port, uname, pwd):
        transport = paramiko.Transport((host, port))
        transport.connect(username=uname, password=pwd)
        self.__sftp = paramiko.SFTPClient.from_transport(transport)

    def connect_by_key(self, host, port, uname, key_path, key_pass = ''):
        key = paramiko.RSAKey.from_private_key_file(key_path, key_pass)
        transport = paramiko.Transport((host, port))
        transport.connect(username=uname, pkey=key)
        self.__sftp = paramiko.SFTPClient.from_transport(transport)

    def get(self, remote, local, cb = None):
        self.__sftp.get(remote, local, cb)

    def put(self, local, remote, cb = None):
        self.__sftp.put(local, remote, cb)