# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 9:56
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import configparser

cp = configparser.ConfigParser()

cfg = """
[test]
a=a;b;c
b=a,b,c

[other]
c=hi
"""

cp.read_string(cfg)

print(cp.sections())

for s in cp.sections():
    for o in cp.options(s):
        print('---', s, o, cp.get(s,o))
