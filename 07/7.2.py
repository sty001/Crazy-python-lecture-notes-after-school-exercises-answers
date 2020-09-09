#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7.2.py
@Time    :   2020/09/09 15:19:20
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

while True:
    str_n = input('请输入整数N: ')
    if str_n == 'exit':
        import sys
        sys.exit(0)
    try:
        n = int(str_n)
        if n % 2 != 0:
            print('有趣')
        elif 5 > n > 2:
            print('没意思')
        elif 20 > n > 6:
            print('有趣')
        else:
            print('没意思')
    except:
        print('务必输入整数')
