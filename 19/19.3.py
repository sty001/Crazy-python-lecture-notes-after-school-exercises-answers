#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   19.3.py
@Time    :   2020/09/09 15:28:48
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

import matplotlib.pyplot as plt
import random

plt.figure()
x_data, y_data = [], []
for i in range(5000): x_data.append(random.uniform(-3, 3))
for i in range(5000): y_data.append(random.uniform(-3, 3))
plt.scatter(x_data, y_data, c='purple', # 设置点的颜色
    s=50, # 设置点半径
    alpha = 0.5, # 设置透明度
    marker='p', # 设置使用五边形标记
    linewidths=1, # 设置边框的线宽
    edgecolors=['green', 'yellow']) # 设置边框的颜色
# 绘制第二个散点图（只包含一个起点），突出起点
plt.scatter(x_data[0], y_data[0], c='red', # 设置点的颜色
    s=150, # 设置点半径
    alpha = 1) # 设置透明度
# 绘制第三个散点图（只包含一个结束点），突出结束点
plt.scatter(x_data[4999], y_data[4999], c='black', # 设置点的颜色
    s=150, # 设置点半径
    alpha = 1) # 设置透明度
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('随机数的散点图')
plt.show()
