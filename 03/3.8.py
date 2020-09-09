#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.8.py
@Time    :   2020/09/09 15:12:32
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import random

char_list = input("请输入空格隔开的大写字母:").split()
char_dict = {}.fromkeys(char_list)
print(char_dict)
for k in char_dict.keys():
    char_dict[k] = char_list.count(k)
print(char_dict)
