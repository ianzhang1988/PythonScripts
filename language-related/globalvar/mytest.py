# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 16:27
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

#import globalvar
#from .globalvar import GlobalVar
from globalvar import GlobalVar
import time

def test():
    print('flag', GlobalVar.kill_task_flag.is_set())
    time.sleep(1)
    print('flag', GlobalVar.kill_task_flag.is_set())

class Test:
    def test(self):
        print('flag', GlobalVar.kill_task_flag.is_set())
        time.sleep(1)
        print('flag', GlobalVar.kill_task_flag.is_set())