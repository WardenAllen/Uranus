# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 10:13
# @Author  : WardenAllen
# @File    : pluto_redis.py
# @Brief   : 

import redis
from .pluto_db import Database

class Redis(Database) :

    def connect(self, uname, pwd, host, port, dbname):
        Database.connect(self, uname, pwd, host, port, dbname)
        self._connect = redis.Redis(
            host=self._host, port=int(self._port), db=int(self._dbname))

    def set(self, k, v):
        self._connect.set(k, v)

    def close(self):
        self._connect.close()

    def ping(self):
        return self.ping()