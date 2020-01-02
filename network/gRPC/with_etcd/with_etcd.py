# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 14:50
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import etcd3
import grpc
import api_pb2
import api_pb2_grpc
import random
import json
from grpc import RpcError


def get_service():
    client = etcd3.client(host='10.18.29.179', port=2379)

    c = client.get_prefix('/etcdv3_resolver/svic.pugc.service/')
    print(type(c))

    service = random.sample(list(c),1)

    print(type(service))
    print(service)

    # [(ip:port, meta)]
    service = service[0][0]
    print(service)

    return service


def main():
    # etcd
    service = get_service()

    with grpc.insecure_channel(service) as channel:
        stub = api_pb2_grpc.JobStub(channel)
        for i in range(10):
            response = stub.GetJob(api_pb2.JobRequest(vid=str(i)))
            print(type(response))
            print(i, response)
            print(type(response.job_info))
            print(i, response.job_info)
            print(' ', response.job_info.job_id, response.job_info.version)
            print(dict(response.job_info))

        put_data = {
            'vid':'1',
            'job_status':0,
        }

        response = stub.PutJob(api_pb2.JobPutRequest(job_put=json.dumps(put_data).encode('utf-8')))
        print("put: ",response)

        response = stub.GetProfile(api_pb2.ProfileGetRequest(name='h'))
        print(response)

if __name__ == '__main__':
    main()