# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 12:02
# @Author  : WardenAllen
# @File    : pluto_ssh.py
# @Brief   : 

import paramiko
from io import StringIO

class PlutoSSH :

    # paramiko's SSHClient() object.
    __ssh = object

    def __init__(self):
        self.__ssh = paramiko.SSHClient()
        self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect_by_pass(self, host, port, uname, pwd):
        self.__ssh.connect(hostname=host, port=port, username=uname, password=pwd)

    def connect_by_key(self, host, port, uname, key_path, key_pass = ''):
        key = paramiko.RSAKey.from_private_key_file(key_path, key_pass)
        self.__ssh.connect(hostname=host, port=port, username=uname, pkey=key)

    def connect_by_key_str(self, host, port, uname, key_str):
        key = paramiko.RSAKey(file_obj=StringIO(key_str))
        self.__ssh = paramiko.SSHClient()
        self.__ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__ssh.connect(host, port, uname, pkey=key)

    def execute(self, cmd):
        stdin, stdout, stderr = self.__ssh.exec_command(cmd)
        res = stdout.read() + stderr.read()
        print(res.decode())