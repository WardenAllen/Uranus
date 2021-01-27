# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 20:07
# @Author  : WardenAllen
# @File    : pluto_db.py
# @Brief   : 

class Database :

    _connect = object
    _is_connect = False
    _username = ''
    _password = ''
    _host = ''
    _port = ''
    _dbname = ''

    def connect(self, uname, pwd, host, port, dbname):
        """
        connect to database.
        :param uname:
        :param pwd:
        :param host:
        :param port:
        :param dbname:
        """
        self._username = uname
        self._password = pwd
        self._host = host
        self._port = port
        self._dbname = dbname

        print('connect to database %s@%s:%s/%s' % (uname, host, port, dbname))

    def execute(self, cmd):
        pass

    def commit(self):
        pass

    def execute_and_commit(self, cmd):
        self.execute(cmd)
        self.commit()

    def fetchall(self):
        pass

    def close(self):
        pass

    def ping(self):
        pass

