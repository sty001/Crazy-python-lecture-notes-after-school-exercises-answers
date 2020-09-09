#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.10.py
@Time    :   2020/09/09 15:14:06
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

radius = int(input("请输入半径: "))
for i in range(2 * radius + 1):
    half = round((radius ** 2 - (radius - i) ** 2) ** 0.5)
    print("  " * (radius - half), end="")
    print("*", end="")
    print("  " * half * 2, end="")
    print("*")
