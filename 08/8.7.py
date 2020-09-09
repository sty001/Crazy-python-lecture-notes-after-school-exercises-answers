#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.7.py
@Time    :   2020/09/09 15:21:44
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


class Point(object):
    ''' 描述点的类 '''

    def __init__(self, x, y):
        ''' 构造器 '''
        self.x = x
        self.y = y

    def __sub__(self, no):
        ''' 为减法提供支持的方法 '''
        return ((self.x - no.x) ** 2 + (self.y - no.y) ** 2) ** 0.5


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 6)
    print(p1 - p2)
    print(p2 - p1)
