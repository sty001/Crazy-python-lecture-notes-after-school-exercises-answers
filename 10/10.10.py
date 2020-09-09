#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.10.py
@Time    :   2020/09/09 15:24:42
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

def fibonacci(n):
    rvt_list = [1, 1]
    # 生成fibonacci数列
    [rvt_list.append(rvt_list[-1] + rvt_list[-2]) for i in range(2, n)]
    return rvt_list
print(fibonacci(10))
# 计算fibonacci数列的元素的平方
x = map(lambda x: x*x , fibonacci(10))
print([e for e in x])