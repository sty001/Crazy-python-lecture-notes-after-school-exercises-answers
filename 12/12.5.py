#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12.5.py
@Time    :   2020/09/09 15:25:55
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from pathlib import *

def process_dir(p):
    for x in p.iterdir():
        if Path(x).is_dir():
            process_dir(Path(x))
        else:
            print(x)
dir_str = input('请输入路径: ')
p = Path(dir_str)
if not p.exists() or not p.is_dir():
    raise ValueError('您输入的不是有效的路径')
process_dir(p)