# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 16:11
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com
import sys
sys.path.append('.')
from other_file import create_data
import tracemalloc

tracemalloc.start()

a = {}

a['a'] = 1
a['b'] = 2

snap1 = tracemalloc.take_snapshot()
top_stats = snap1.statistics('lineno')
for stat in top_stats[:10]:
     print(stat)

print("----------------------------")

data = []

def helper():
    for i in range(9999):
        data.append(i)

helper()
data.append(1)

snap2 = tracemalloc.take_snapshot()
top_stats = snap2.compare_to(snap1,'lineno')
for stat in top_stats[:10]:
     print(stat)

print("----------------------------")

data2 = create_data()

snap3 = tracemalloc.take_snapshot()
top_stats = snap3.compare_to(snap2,'lineno')
for stat in top_stats[:10]:
     print(stat)

top_stats = tracemalloc.take_snapshot().statistics('lineno')
for stat in top_stats[:10]:
     print(stat)