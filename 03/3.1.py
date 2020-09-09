#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   3.1.py
@Time    :   2020/09/09 15:11:46
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

a, b, c = input("请输入第一个字符串:"), input("请输入第二个字符串:"), input("请输入第三个字符串:")
# 创建元组
tuple1 = (a, b, c)
print(tuple1 * 3)
# 创建元组
tuple2 = ("fkjava", "crazyit")
# 合并两个元组
print(tuple1 + tuple2)
