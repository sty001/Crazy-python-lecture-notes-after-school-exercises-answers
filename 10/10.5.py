#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.5.py
@Time    :   2020/09/09 15:24:12
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import re
string, sub = input("请输入第一个字符串: "), input('请输入子串: ')
matches = list(re.finditer(r'(?={})'.format(sub), string))
if matches:
    print('\n'.join(str((match.start(),
        match.start() + len(sub) - 1)) for match in matches))
else:
    print('(-1, -1)')