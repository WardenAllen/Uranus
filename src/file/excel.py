# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 11:36
# @Author  : WardenAllen
# @File    : excel.py
# @Brief   : Excel file's reader and writer

import xlrd
import time
from xlrd import xldate_as_tuple
from datetime import datetime

class Excel:

    # excel file's name.
    __name: str = ''

    # xlrd variable.
    __book : xlrd.book.Book()

    # parsed data.
    __data = []

    # time parsed into timestamp by default.
    __use_timestamp = True

    def __init__(self, ts = True):
        self.__use_timestamp = ts

    def __read_int(self, row, key, val):
        self.__data[row][key] = int(val)

    def __read_float(self, row, key, val):
        self.__data[row][key] = float(val)

    def __read_string(self, row, key, val):
        self.__data[row][key] = str(val)

    def __read_time(self, row, key, val):
        date = xldate_as_tuple(val, 0)

        if self.__use_timestamp :
            self.__data[row][key] = int(time.mktime(datetime(*date).timetuple()))
        else :
            self.__data[row][key] = datetime(*date)

    def open(self, file):
        try:
            self.__book = xlrd.open_workbook(file)
        except IOError:
            print("open failed")
            exit(1)

    def read(self, sheet_num = 0):
        self.__data = []

        sheet = self.__book.sheets()[sheet_num]

        for i in range(0, sheet.nrows):
            self.__data.append(dict())

        keys = sheet.row_values(0)
        types = sheet.row_values(1)

        for i in range(sheet.nrows)[2:]:
            row_values = sheet.row_values(i)
            for j in range(0, sheet.ncols):

                #invalid key or comment key.
                if len(keys[j]) == 0 or keys[j][0] == '#' :
                    continue

                name = '_Excel__read_' + str(types[j]).lower()
                if hasattr(self, name) :
                    getattr(self, name) (i, keys[j], row_values[j])

        self.__data = self.__data[2:]
        return self.__data

    def clear(self):
        self.__name = ''
        self.__book.close()
        self.__data = []