#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.4.py
@Time    :   2020/09/09 15:12:07
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
    num = random.randint(0, 200)
    if num % 2 == 0:
        my_list.append(num + 1)
    else:
        my_list.append(num)
print(my_list)
my_list = [random.randint(0, 100) * 2 + 1 for i in range(length)]
print(my_list)
