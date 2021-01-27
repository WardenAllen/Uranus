# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 19:15
# @Author  : WardenAllen
# @File    : http_client.py
# @Brief   : 

import requests

def post(_url, _data) :
    return requests.post(_url, _data)
