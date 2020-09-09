#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10.1.py
@Time    :   2020/09/09 15:23:54
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import json

name = input('请输入您的名字: ')
while True:
    try:
        age = int(input('请输入您的年龄: '))
        break
    except:
        print('年龄需要您输入整数')
while True:
    try:
        height = float(input('请输入您的身高: '))
        break
    except:
        print('身高需要您输入浮点数')
with open('my.txt', 'w+') as f:
    json.dump({'name': name, 'age': age, 'height': height}, f)

with open('my.txt', 'r') as f:
    my_info = json.load(f)
    print(my_info['name'])
    print(my_info['age'])
    print(my_info['height'])