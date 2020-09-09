#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   4.7.py
@Time    :   2020/09/09 15:13:41
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

start = 101
end = 200
for i in range(101, end + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)
