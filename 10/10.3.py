#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.3.py
@Time    :   2020/09/09 15:24:03
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import re, sys

while True:
    string = input('请输入手机号: ')
    if string == 'exit':
        sys.exit(0)
    if re.fullmatch('^(1[358][0-9]|14[579]|16[6]|17[0135678]|19[89])\d{8}$', string):
        print('是手机号码')
    else:
        print('不是手机号码')
    