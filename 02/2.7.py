#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2.7.py
@Time    :   2020/09/09 15:11:39
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

# 原字符串
string = input("请输入原字符串:")
i, character = input("请输入位置和替换字符：").split()
position = int(i)
str_new = string[:position] + character + string[position+1:]
print(str_new)
