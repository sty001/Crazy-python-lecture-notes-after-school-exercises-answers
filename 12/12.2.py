#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12.2.py
@Time    :   2020/09/09 15:25:36
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import os, sys

print('请开始逐行地输入内容')
f = open('my.txt', 'w+')
while True:
    string = input()
    if string == 'exit':
        sys.exit(0)
        f.close()
    f.write(string + os.linesep)
