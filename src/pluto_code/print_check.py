# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 15:10
# @Author  : WardenAllen
# @File    : print_check.py
# @Brief   : check whether param num match format(%) num.

import file.pluto_file as pfile

def _strip(line):
    return line.strip('\r').strip('\n').strip('\t').lstrip().rstrip()

def print_check(_file, _keyword):

    file = open(_file, encoding='UTF-8', errors="ignore")

    line = file.readline()  # 调用文件的 readline()方法
    ln = 1

    while line:

        line = _strip(line)

        if line.find(_keyword) != -1:

            # code might not finished.
            if line.find(';') == -1:
                while True:
                    nl = _strip(file.readline())
                    ln += 1
                    line += nl
                    if nl.find(';') != -1:
                        break

            if line.count('%') != line.count(',') :
                print("%s Line %d %s %d" % (_file, ln, line, line.find(_keyword)))
                print("fmt:%d param:%d", line.count('%'), line.count(','))
        #
        #     line = line.replace('/root/projects/ProjectA/ProjectA/', '')
        #     text.append(line + '\n')

        line = file.readline()
        ln += 1

    file.close()

def flt(isfile, name) :
    if not isfile : return False
    return name.find('.cpp') == -1

if __name__ == '__main__':

    folder = "C:/Users/admin/Desktop/Project/Server/Mainline"
    filse = pfile.list_files(folder, True, True, flt)

    for f in filse:
        print_check(f, 'LogInfo')

