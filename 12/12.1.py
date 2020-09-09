#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12.1.py
@Time    :   2020/09/09 15:25:29
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

with open('text1.txt') as f1:
    text1 = f1.read()
with open('text2.txt') as f2:
    text2 = f2.read()
rvt = (list(text1) + list(text2))
rvt.sort()
with open('text3.txt', 'w+') as f3:
    f3.write("".join(rvt))
