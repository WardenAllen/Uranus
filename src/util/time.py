# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 15:17
# @Author  : WardenAllen
# @File    : time.py
# @Brief   : time utils.

import datetime
import time

FORMAT_DATE = '%Y-%m-%d'
FORMAT_SEC  = '%Y-%m-%d %H:%M:%S'
FORMAT_MS   = '%Y-%m-%d %H:%M:%S.%f'

def now_ns():
    return int(time.time() * 1000000000)

def now_us():
    return int(time.time() * 1000000)

def now_ms():
    return int(time.time() * 1000)

def now():
    return int(time.time())

def now_str():
    return datetime.datetime.now().strftime(FORMAT_SEC)

def now_ms_str():
    return datetime.datetime.now().strftime(FORMAT_MS)

def today():
    return datetime.datetime.now().strftime(FORMAT_DATE)

def ts_from_str(s):
    """
    Get timestamp in second from time string.
    :param s:   time in string.
    :return:    timestamp in second.
    """
    return int(time.mktime(time.strptime(s, FORMAT_SEC)))

def str_from_ts(ts):
    """
    Get time string from timestamp in second.
    :param ts:  timestamp in second.
    :return:    time in string.
    """
    return time.strftime(FORMAT_SEC, time.localtime(ts))