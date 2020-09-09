#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   5.4.py
@Time    :   2020/09/09 15:15:34
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def count_str_char(string):
    char_num, digit_num, space_num, other_num = 0, 0, 0, 0
    for c in string:
        if c.isdigit():
            digit_num += 1
        elif c.isalpha():
            char_num += 1
        elif c.isspace():
            space_num += 1
        else:
            other_num += 1
    return char_num, digit_num, space_num, other_num


while(True):
    string = input("请输入一个字符串:")
    if string == 'exit':
        import sys
        sys.exit(0)
    char_num, digit_num, space_num, other_num = count_str_char(string)
    print('字母个数', char_num)
    print('数字个数', digit_num)
    print('空白个数', space_num)
    print('其他字母个数', other_num)
