# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 11:59
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

# import hyper
#
# c = hyper.HTTP20Connection('127.0.0.1', 50051)
# rep = c.request('GET', '/')
# print(type(rep))
# print(rep)

from hyper import HTTPConnection,HTTP20Connection

conn = HTTP20Connection('127.0.0.1', port=50051)
id = conn.request('GET', '/')
print(id)
resp = conn.get_response(id)

print(resp.read())