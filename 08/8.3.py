#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.3.py
@Time    :   2020/09/09 15:19:47
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


class Sums:
    def __init__(self, len):
        self.current_index = 1
        self.current_value = 0
        self.__len = len
    # 定义迭代器所需的__next__方法

    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算：
        self.current_value += self.current_index
        self.current_index += 1
        # 数列长度减1
        self.__len -= 1
        return self.current_value
    # 定义__iter__方法，该方法返回迭代器

    def __iter__(self):
        return self


sums = Sums(10)
# 获取迭代器的下一个元素
print(next(sums))
for el in sums:
    print(el, end=' ')
