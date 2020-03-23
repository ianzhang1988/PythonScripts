# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 16:26
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import globalvar
from mytest import test
import threading

t = threading.Thread(target=test)
t.start()

globalvar.kill_task()

t.join()




