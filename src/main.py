# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:55
# @Author  : WardenAllen
# @File    : main.py
# @Brief   : 

from db.pluto_mysql import *

if __name__ == '__main__':

    m = MySQL()
    m.connect('root', '123456@Ab', '192.168.1.24', '3306', 'test')
    # m.execute_and_commit('INSERT INTO user(name) VALUES("123")')

    m.execute('SELECT * FROM user')
    print(m.fetchall())
    m.commit()

    # e = excel.Excel()
    # e.open('server_list.xlsx')
    # d = e.read()
