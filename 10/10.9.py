#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.9.py
@Time    :   2020/09/09 15:24:37
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from collections import Counter

string = input('请输入一个字符串: ')
c = Counter(string)
[print(t[0]) for t in c.most_common(3)]