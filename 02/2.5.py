#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2.5.py
@Time    :   2020/09/09 15:11:22
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

string, sub_string = input("请输入字符串:"), input("请输入子串:")
# 字符串长度
str_len = len(string)
# 子串长度
sub_str_len = len(sub_string)
ct = 0
for i in range(str_len-1):
    # 每次取和子字符串长度相等的字符串和子字符串进行比较
    if string[i:i + sub_str_len] == sub_string:
        ct += 1
print("子串在字符串中出现的次数：%d" % ct)
