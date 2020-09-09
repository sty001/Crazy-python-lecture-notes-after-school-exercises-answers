#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.7.py
@Time    :   2020/09/09 15:15:55
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def remove_duplicate(source_list):
    new_list = list({}.fromkeys(source_list).keys())
    return new_list
    # 另一种方法
#    new_list = []
#    [new_list.append(i) for i in source_list if not i in new_list]
#    return new_list


length = int(input("请输入列表的长度:"))
my_list = []
for i in range(length):
    my_list.append(input('请输入字符串:'))
print(remove_duplicate(my_list))
