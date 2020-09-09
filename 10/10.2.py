#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.2.py
@Time    :   2020/09/09 15:23:59
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import re, sys

while True:
    string = input('输入字符串: ')
    if string == 'exit':
        sys.exit(0)
    if not re.fullmatch('[0-9,\.]+', string):
        raise ValueError("您的输入只能包含0-9数字、英文逗号、英文点号")
    rt_list = re.findall('[0-9]+', string)
    print(rt_list)