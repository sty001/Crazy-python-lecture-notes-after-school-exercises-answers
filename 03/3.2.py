#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.2.py
@Time    :   2020/09/09 15:11:53
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

# 给定一个list
list1 = ["fkjava", "crazyit", "hello", "world", "python"]
start, end = int(input("输入start:")), int(input("输入end:"))
# 复制
list2 = list1[start: end]
print(list2)
