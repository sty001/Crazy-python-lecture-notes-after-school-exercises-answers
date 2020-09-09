#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.2.py
@Time    :   2020/09/09 15:12:44
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

lines = int(input("输入要打印的行数:"))
for i in range(lines):
    for j in range(0, lines - i):
        print(end=" ")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
