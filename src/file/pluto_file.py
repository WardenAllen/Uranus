# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 11:10
# @Author  : WardenAllen
# @File    : pluto_file.py
# @Brief   : 

import os
import shutil

def _search(_path,
            _files,
            _folders,
            _recursive,
            _prifix,
            _filter) :
    for f in os.listdir(_path):
        abspath = os.path.join(_path, f)
        if os.path.isfile(abspath):
            if _filter and _filter(True, f) : continue
            _files.append(abspath if _prifix else f)
        elif os.path.isdir(abspath):
            if _filter and _filter(False, f): continue
            _folders.append(abspath if _prifix else f)
            if _recursive :
                _search(abspath, _files, _folders, _recursive, _prifix, _filter)

def list_files(_path,
               _recursive = False,
               _prifix = False,
               _filter = None) :
    """
    Get all files from target path.
    :param _path:            path to search.
    :param _recursive:       whether search recursively.
    :param _prifix:          whether has prifix (path) name.
    :param _filter:          filter funtion, first argument
                             MUST BE BOOL means whether it's file.
    """
    files = []
    _search(_path, files, [], _recursive, _prifix, _filter)
    print('total files %d:' % len(files))
    for f in files : print(f)
    return files

def list_folders(_path,
                 _recursive = False,
                 _prifix = False,
                 _filter = None) :
    """
    Get all folders from target path.
    :param _path:        path to search.
    :param _recursive:   whether search recursively.
    :param _prifix:      whether has prifix (path) name.
    :param _filter:          filter funtion.
    """
    folders = []
    _search(_path, [], folders, _recursive, _prifix, _filter)
    print('total folders %d:' % len(folders))
    for f in folders: print(f)
    return folders

def move_file(_src, _dst):

    if not os.path.isfile(_src) : return
    return shutil.move(_src, _dst)

def move_folder(_src, _dst,
                _recursive = False,
                _filter=None) :

    if not os.path.isdir(_src) : return

    files = list_files(_src, _recursive, True, _filter)
    for f in files: move_file(f, str(f).replace(_src, _dst))

