#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.1.py
@Time    :   2020/09/09 15:14:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def choose_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        for j in range(i + 1, list_len):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


list1 = [3, 6, 1, 8, 5, -20, 100, 50, 200]
choose_sort(list1)
print(list1)
