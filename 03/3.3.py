#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.3.py
@Time    :   2020/09/09 15:12:00
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
    # 获得一个随机数
    num = random.random()
    my_list.append(num)
print(my_list)
my_list = [random.random() for i in range(length)]
print(my_list)
