#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.1.py
@Time    :   2020/09/09 15:12:39
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

for i in range(1, 10):
    for j in range(1, i+1):
        print("%2d * %2d = %2d" % (j, i, i * j), end=" ")
    print()
