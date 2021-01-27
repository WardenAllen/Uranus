# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 14:53
# @Author  : WardenAllen
# @File    : config.py
# @Brief   : Config file generators.

import toml
import json
import datetime

def write_toml(obj, file) :
    """
    generate toml data into file.
    :param obj:     object to generate.
    :param file:    file name.
    """
    with open(file, "w", encoding="utf-8") as fs:
        toml.dump(obj, fs)

class DateEncoder(json.JSONEncoder) :
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

def write_json(obj, file) :
    """
    generate json data into file.
    :param obj:       object to generate.
    :param file:    file name.
    """
    with open(file, "w", encoding="utf-8") as fs:
        json.dump(obj, fs, cls = DateEncoder)

def write_json(obj) :
    return json.dumps(obj)

def read_toml(file) :
    with open(file, "r", encoding="utf-8") as fs:
        obj = toml.load(fs)
    return obj

def read_json(file) :
    with open(file, "r", encoding="utf-8") as fs:
        obj = json.load(fs)
    return obj

