#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.6.py
@Time    :   2020/09/09 15:13:13
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

while(True):
    s = input("输入自己的成绩:")
    if s == 'exit':
        import sys
        sys.exit(0)
    score = float(s)
    if score >= 90:
        print('A')
    elif 90 > score >= 80:
        print('B')
    elif 80 > score >= 70:
        print('C')
    else:
        print('D')
