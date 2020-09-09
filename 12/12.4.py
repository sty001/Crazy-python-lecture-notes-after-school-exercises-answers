#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12.4.py
@Time    :   2020/09/09 15:25:47
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from pathlib import *
import re, os

phone_pattern = '1[358][0-9]\d{8}|14[579]\d{8}|16[6]\d{8}|17[0135678]\d{8}|19[89]\d{8}'
f = open('phones.txt', 'w+')
def process_dir(p):
    for x in p.iterdir():
        if Path(x).is_dir():
            process_dir(Path(x))
        else:
            try:
                content = Path(x).read_text(encoding='GBK')
                phone_list = re.findall(phone_pattern, content)
                for x in phone_list: f.write(x + os.linesep)
            except:
                try:
                    content = Path(x).read_text(encoding='GBK')
                    phone_list = re.findall(phone_pattern, content)
                    for x in phone_list: f.write(x + os.linesep)
                except:
                    pass
dir_str = input('请输入路径: ')
p = Path(dir_str).strip()
if not p.exists() or not p.is_dir():
    raise ValueError('您输入的不是有效的路径')
process_dir(p)
f.close()