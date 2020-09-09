#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.6.py
@Time    :   2020/09/09 15:24:17
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import re

python_set = set(re.findall('[^,\.\s]+', input('学习Python的学员: ')))
java_set = set(re.findall('[^,\.\s]+', input('学习Java的学员: ')))
print(python_set)
print(java_set)
diff = python_set - java_set
print('只学Python不学Java的学员:', diff)
print('只学Python不学Java的学员有%d人' % len(diff))