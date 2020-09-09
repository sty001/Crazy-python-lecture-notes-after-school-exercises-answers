#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.9.py
@Time    :   2020/09/09 15:14:00
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

string = input("请输入一行内容: ")
char_num, digit_num, other_num = 0, 0, 0
for c in string:
    if c.isdigit():
        digit_num += 1
    elif c.isalpha():
        char_num += 1
    else:
        other_num += 1
print('字母个数', char_num)
print('数字个数', digit_num)
print('其他字母个数', other_num)
