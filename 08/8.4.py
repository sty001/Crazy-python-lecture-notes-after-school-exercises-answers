#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.4.py
@Time    :   2020/09/09 15:19:54
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def card_generator():
    nums = 52
    flowers = ('♠', '♥', '♣', '♦')
    values = ('2', '3', '4', '5',
              '6', '7', '8', '9',
              '10', 'J', 'Q', 'K', 'A')
    for i in range(nums):
        yield flowers[i // 13] + values[i % 13]


if __name__ == '__main__':
    cg = card_generator()
    print(next(cg))  # ♠2，生成器“冻结”在yield处
    print(next(cg))  # ♠3，生成器再次“冻结”在yield处
    for ele in cg:
        print(ele, end=' ')
