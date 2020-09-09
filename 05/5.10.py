#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.10.py
@Time    :   2020/09/09 15:16:13
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
import random


def fn(n):
    # 输出矩阵
    for i in range(n):
        for j in range(n):
            print(' %2d ' % (i * n + j + 1), end="")
        print()
    print('-' * (4 * n))
    # 输出转置矩阵
    for i in range(n):
        for j in range(n):
            print(' %2d ' % (j * n + i + 1), end="")
        print()


n = int(input("请输入整数n:"))
fn(n)
