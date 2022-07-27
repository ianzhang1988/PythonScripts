# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 18:39
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from tornado import httpclient
http_client = httpclient.HTTPClient()
try:
    response = http_client.fetch('http://127.0.0.1:7777/pic/100.jpg')
    print(response.body)
except httpclient.HTTPError as e:
    print("Error:", e)
http_client.close()

with open('test.jpg', 'wb') as f:
    f.write(response.body)