#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7.1.py
@Time    :   2020/09/09 15:19:14
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

str_n = input('请输入整数N: ')
try:
    n = int(str_n)
    print(n)
    i = 0
    while True:
        try:
            a, b = input('请输入2个整数(空格隔开): ').split()
            print(int(a) // int(b))
            i += 1
            if i >= n:
                break
        except:
            print('务必输入空格隔开的2个整数!')
except:
    print('请输入整数N!')
