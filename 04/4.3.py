#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.3.py
@Time    :   2020/09/09 15:12:50
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

size = int(input("输入要打印的SIZE(奇数):"))
array = [[0] * size]
# 创建一个长度size * size的二维列表
for i in range(size - 1):
    array += [[0] * size]
row, col = 0, size // 2
for i in range(1, size * size + 1):
    array[row][col] = i
    if i % size == 0:
        row += 1
    elif row == 0:
        row = size - 1
        col += 1
    elif col == size - 1:
        row -= 1
        col = 0
    else:
        row -= 1
        col += 1
for i in range(size):
    for j in range(size):
        print('%02d' % array[i][j], end=" ")
    print()
