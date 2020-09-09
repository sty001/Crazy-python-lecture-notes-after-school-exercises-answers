#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   7.3.py
@Time    :   2020/09/09 15:19:24
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def fn(tp):
    for e in tp:
        if not isinstance(e, str):
            raise ValueError('所有元素必须是字符串')
        if not (20 >= len(e) >= 6):
            raise ValueError('字符串的长度必须在6～20之间')
    print(tp)


if __name__ == '__main__':
    fn(('fkjava', 'crazyit'))
#    fn((20,))
    fn(('fkjavafkjavafkjavafkjava'))
