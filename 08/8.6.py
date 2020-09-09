#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.6.py
@Time    :   2020/09/09 15:21:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import os


def files_generator():
    for filename in os.listdir(r'.'):
        yield filename


if __name__ == '__main__':
    fg = files_generator()
    print(next(fg))  # 8.1.py，生成器“冻结”在yield处
    print(next(fg))  # 8.2.py，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')
