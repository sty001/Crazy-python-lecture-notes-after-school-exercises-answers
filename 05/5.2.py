#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.2.py
@Time    :   2020/09/09 15:14:41
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def bubble_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        is_sorted = True
        for j in range(0, list_len - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_sorted = False
        if is_sorted:
            return


list1 = [3, 6, 1, 8, 5, -20, 100, 50, 200, -32, 123]
bubble_sort(list1)
print(list1)
