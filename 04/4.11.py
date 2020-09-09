#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.11.py
@Time    :   2020/09/09 15:14:12
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

lines = int(input("请输入一半的行数: "))
# 打印上半
for i in range(lines):
    print("-" * (lines * 2 - 2 - 2 * i), end="")
    my_list = []
    for j in range(i + 1):
        my_list.append(chr(96 + lines - j))
    for j in range(i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (lines * 2 - 2 - 2 * i))
# 打印下半
for i in range(lines - 1):
    print("-" * (2 * (i + 1)), end="")
    # 换一种方式初始化list列表
    my_list = [chr(96 + lines - j) for j in range(lines - 1 - i)]
    for j in range(lines - 2 - i):
        my_list.append(chr(ord(my_list[-1]) + 1))
    print('-'.join(my_list), end="")
    print("-" * (2 * (i + 1)))
