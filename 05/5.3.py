#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.3.py
@Time    :   2020/09/09 15:14:49
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def is_leap(year):
    year = int(year)
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


while(True):
    year = input("请输入一个年份:")
    if year == 'exit':
        import sys
        sys.exit(0)
    print("%s是闰年吗? %s" % (year, is_leap(year)))
