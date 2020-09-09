#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.5.py
@Time    :   2020/09/09 15:15:44
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def fn(n):
    if n < 2:
        exit()
    sum = 1
    for i in range(2, n+1):
        sum += i ** 3
    return sum


n = int(input("请输入数字:"))
result = fn(n)
print("1～%d的立方和是%d" % (n, result))
