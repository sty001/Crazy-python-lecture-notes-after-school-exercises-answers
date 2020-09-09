#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.5.py
@Time    :   2020/09/09 15:13:07
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

lines = int(input("输入要打印的行数(奇数):"))
if lines % 2 == 0:
    print('请输入奇数')
    import sys
    sys.exit(0)
half_lines = lines // 2 + 1
# 打印上半
for i in range(half_lines):
    print(" " * (half_lines - i), end="")
    if i == 0:
        print("*")
    else:
        print("*", end="")
        print(" " * (2 * i - 1), end="")
        print("*")
# 打印下半
for i in range(half_lines - 1):
    print(" " * (i + 2), end="")
    if i == half_lines - 2:
        print("*")
    else:
        print("*", end="")
        print(" " * (lines - 4 - 2 * i), end="")
        print("*")
