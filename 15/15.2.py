#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   15.2.py
@Time    :   2020/09/09 15:28:13
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from urllib.request import *
import re

with urlopen('http://www.crazyit.org/index.php') as f:
    # 按字节读取数据
    data = f.read()
    # 将字节数据恢复成字符串
    content = data.decode('utf-8')
    link_pattern = '<a\s+href=\"([a-zA-Z0-9\.:\?&=\-;/%]+)\"'
    it = re.finditer(link_pattern, content)
    for m in it:
        print(m.group(1))
