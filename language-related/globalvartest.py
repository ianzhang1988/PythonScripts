# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 16:32
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import globalvar.globalvar as GlobalVar
#from globalvar.mytest import test
from globalvar.mytest import Test
import threading

tt = Test()

t = threading.Thread(target=tt.test)
t.start()

# GlobalVar.kill_task()

def kill():
    GlobalVar.kill_task()

t2 = threading.Thread(target=kill)
t2.start()

t.join()
t2.join()