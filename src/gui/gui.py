# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 15:38
# @Author  : WardenAllen
# @File    : gui.py
# @Brief   : 

from tkinter import *
from tkinter import ttk

class PlutoGui :

    _root = object

    def __init__(self):
        pass

    def init(self, title, geo=''):
        self._root = Tk()
        self._root.title(title)
        if len(geo) != 0: self._root.geometry(geo)

    def run(self):
        self._root.mainloop()

    def add_progress_bar(self, orient="horizontal"):
        progress_bar = ttk.Progressbar(self._root,
                                       orient=orient,
                                       mode="determinate")
        progress_bar.pack(side=TOP, fill=X)
        progress_bar["maximum"] = 100
        progress_bar["value"] = 0
