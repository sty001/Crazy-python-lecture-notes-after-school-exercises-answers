#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.4.py
@Time    :   2020/09/09 15:24:08
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import re, sys

while True:
    string = input('请输入字符串: ')
    if string == 'exit':
        sys.exit(0)
    m2 = re.search('[a-zA-Z]', string)
    if m2:
        print(m2.group())

    