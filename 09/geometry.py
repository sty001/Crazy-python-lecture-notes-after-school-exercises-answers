#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   geometry.py
@Time    :   2020/09/09 15:22:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

'''
这是geometry模块：
print_triangle(n): 用星号打印三角形
print_diamand(n): 用星号打印菱形
'''


def print_triangle(n):
    '''
    用星号打印三角形的函数
    n - 控制三角形的高度。
    '''
    for i in range(n):
        for j in range(0, n - i):
            print(end=" ")
        for k in range(2 * i + 1):
            print("*", end="")
        print()


def print_diamand(n):
    '''
    用星号打印菱形的函数
    n - 控制菱形的高度，该高度必须是奇数
    '''
    if n % 2 == 0:
        raise ValueError('参数n必须是奇数')
    half_lines = n // 2 + 1
    # 打印上半
    for i in range(half_lines):
        print(" " * (half_lines - i), end="")
        print("*" * (2 * i + 1))
    # 打印下半
    for i in range(half_lines - 1):
        print(" " * (i + 2), end="")
        print("*" * (n - 2 - 2 * i))
