# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 20:33
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

for i in range(5):
    print(i)
    if i > 2:
        raise Exception('exc')
finally:
    print('----- else here')