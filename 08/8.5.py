#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.5.py
@Time    :   2020/09/09 15:21:29
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def factorial_generator(n):
    rvt_list = [1]
    for i in range(2, n + 1):
        rvt_list.append(rvt_list[-1] * i)
    print('------------', len(rvt_list))
    for i in range(n):
        yield rvt_list[i]


if __name__ == '__main__':
    fg = factorial_generator(10)
    print(next(fg))  # 1，生成器“冻结”在yield处
    print(next(fg))  # 2，生成器再次“冻结”在yield处
    for ele in fg:
        print(ele, end=' ')
