#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.6.py
@Time    :   2020/09/09 15:15:49
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def fn(n):
    result_list = [1]
    for i in range(n):
        result_list.append(result_list[-1] * len(result_list))
    return result_list[-1]


n = int(input("请输入数字:"))
result = fn(n)
print("%d的阶乘是%d" % (n, result))
