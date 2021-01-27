# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 19:33
# @Author  : WardenAllen
# @File    : pluto_mysql.py
# @Brief   : 

import pymysql
from .pluto_db import Database

class MySQL(Database) :

    __cursor = object

    def connect(self, uname, pwd, host, port, dbname):
        Database.connect(self, uname, pwd, host, port, dbname)
        self._connect =  pymysql.connect(
            host=self._host, user=self._username, passwd=self._password,
            db=self._dbname, port=int(self._port), charset='utf8')
        self.__cursor = self._connect.cursor()

    def execute(self, cmd):
        self.__cursor.execute(cmd)

    def commit(self):
        self._connect.commit()

    def fetchall(self):
        return self.__cursor.fetchall()

    def close(self):
        self._connect.close()

    def ping(self):
        self._connect.ping()

