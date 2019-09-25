# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 14:53
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import etcd3

# client = etcd.Client() # this will create a client against etcd server running on localhost on port 4001

client = etcd3.client(host='10.18.29.179', port=2379)
#client = etcd.Client(host=(('127.0.0.1', 4001), ('127.0.0.1', 4002), ('127.0.0.1', 4003)))
#client = etcd.Client(host='127.0.0.1', port=4003, allow_redirect=False) # wont let you run sensitive commands on non-leader machines, default is true
# If you have defined a SRV record for _etcd._tcp.example.com pointing to the clients
#client = etcd.Client(srv_domain='example.com', protocol="https")
# create a client against https://api.example.com:443/etcd
# client = etcd.Client(host='api.example.com', protocol='https', port=443, version_prefix='/etcd')


# c = client.read('', recursive = True)
# print(type(c))
# print(c)

c = client.get('/etcdv3_resolver/svic.pugc.service/10.18.29.179:9000')
print(type(c))
print(c[0])

c = client.get_prefix('/etcdv3_resolver/svic.pugc.service/')
print(c)
print (list(c))

# for i in c:
#     print(i)


