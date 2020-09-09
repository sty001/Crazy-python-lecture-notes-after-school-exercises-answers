#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   8.1.py
@Time    :   2020/09/09 15:19:35
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib


def check_key(key):
    if not isinstance(key, int):
        raise TypeError('索引值必须是整数')
    if key < 0:
        raise IndexError('索引值必须是非负整数')
    if key >= 52:
        raise IndexError('索引值不能超过%d' % 52)


class CardSeq:
    def __init__(self):
        self.flowers = ('♠', '♥', '♣', '♦')
        self.values = ('2', '3', '4', '5',
                       '6', '7', '8', '9',
                       '10', 'J', 'Q', 'K', 'A')
        self.__changed = {}
        self.__deleted = []

    def __len__(self):
        return 52

    def __getitem__(self, key):
        check_key(key)
        # 如果在self.__changed中找到已经修改后的数据
        if key in self.__changed:
            return self.__changed[key]
        # 如果key在self.__deleted中，说明该元素已被删除
        if key in self.__deleted:
            return None
        # 否则根据计算规则返回序列元素
        flower = key // 13
        value = key % 13
        return self.flowers[flower] + self.values[value]

    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value

    def __delitem__(self, key):
        check_key(key)
        # 如果__deleted列表中没有包含被删除key，添加被删除的key
        if key not in self.__deleted:
            self.__deleted.append(key)
        # 如果__changed中包含被删除key，删除它
        if key in self.__changed:
            del self.__changed[key]


if __name__ == '__main__':
    cq = CardSeq()
    print(len(cq))
    print(cq[2])  # '♠4'
    print(cq[1])  # '♠3'
    # 修改cq[1]元素
    cq[1] = '♣2'
    # 打印修改之后的cq[1]
    print(cq[1])  # '♣2'
    # 删除cq[1]
    del cq[1]
    print(cq[1])  # None
    # 再次对cq[1]赋值
    cq[1] = '♦5'
    print(cq[1])  # ♦5
