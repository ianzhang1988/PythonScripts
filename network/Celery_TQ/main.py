# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 18:37
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com
import sys
sys.path.append('myTQ')

from myTQ.app import add, app

if __name__ == "__main__":
    print(add)
    ret = add.delay(1,2)
    print("ret:",ret.get())

    ret = app.send_task("myTQ.app.add", args=(1, 2))
    print("send_task ret:", ret.get())