#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.6.py
@Time    :   2020/09/09 15:12:19
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import random

length = int(input("请输入列表的长度:"))
my_list = []
for i in range(length):
    my_list.append(input('请输入字符串:'))
print(my_list)
new_list = []
[new_list.append(i) for i in my_list if not i in new_list]
print(new_list)

# 另一种方法
new_list = list({}.fromkeys(my_list).keys())
print(new_list)
