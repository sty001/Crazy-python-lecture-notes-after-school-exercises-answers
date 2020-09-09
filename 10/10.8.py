#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.8.py
@Time    :   2020/09/09 15:24:32
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input('请输入要比较几组:'))):
    print(int(abs((dt.strptime(input('第一个时间:'), fmt) - 
        dt.strptime(input('第二个时间:'), fmt)).total_seconds())))