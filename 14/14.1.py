#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14.1.py
@Time    :   2020/09/09 15:27:40
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib

from concurrent.futures import ThreadPoolExecutor
import threading

class PrintUtil:
    def __init__(self):
        # 正在打印的值
        self.number = 0
        # 控制应由哪个线程执行该任务
        self.state = 1
        self.cond = threading.Condition()
    def print(self, thread_num):
        try:
            self.cond.acquire()
            while self.state != thread_num :
                self.cond.wait()
            # 打印5个连续数值
            for i in range(5):
                self.number += 1
                print("thread%d : %d" % (thread_num, self.number))
            # 每打印5个数字，state加1，控制轮到下一个线程来执行打印
            self.state = self.state % 3 + 1
            self.cond.notify_all()
        finally:
            self.cond.release()
def action(pu, thread_num):
    # 控制每个线程要执行PrintUtil对象的print()方法5次
    for i in range(5):
        pu.print(thread_num)

pu = PrintUtil()
# 创建一个包含3条线程的线程池
with ThreadPoolExecutor(max_workers=3) as pool:
    # 启动3条线程
    for i in range(3):
        # 使用线程池启动3条线程
        pool.submit(action, pu, i + 1)
