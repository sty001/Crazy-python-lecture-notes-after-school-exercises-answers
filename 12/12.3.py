#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12.3.py
@Time    :   2020/09/09 15:25:42
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from pathlib import *
import re, os, sys, codecs

phone_pattern = '1[358][0-9]\d{8}|14[579]\d{8}|16[6]\d{8}|17[0135678]\d{8}|19[89]\d{8}'

dir_str = input('请输入文件路径: ').strip()
p = Path(dir_str)
if not p.exists() or not p.is_file():
    raise ValueError('您输入的不是有效的文件')
def read_phones(f, wf):
    while True:
        line = f.readline()
        # 如果没有读到数据，跳出循环
        if not line: break
        phone_list = re.findall(phone_pattern, line)
        for x in phone_list: wf.write(x + os.linesep)
    f.close()
with open('phone.txt', 'w+') as wf:
    # 目标文件内容可能很大，故逐行读取，尝试用gbk或utf-8两种字符集读取
    try:
        f = codecs.open(dir_str, 'r', 'gbk', buffering=True)
        read_phones(f, wf)
    except:
        try:
            f = codecs.open(dir_str, 'r', 'utf-8', buffering=True)
            read_phones(f, wf)
        except:
            print('该文件不是文本文件')
            sys.exit(0)

