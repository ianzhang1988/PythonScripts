# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 10:34
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import requests
import shutil
import time

def download_file(url):
    local_filename = url.split('/')[-1]
    local_filename='test'
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def download_file2(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

def download_file3(url):
    local_filename = url.split('/')[-1]
    local_filename = 'test'
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True, headers={'Connection': 'close'}) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

if __name__ == '__main__':
    # begin = time.time()
    # local_filename = download_file3('http://sdn077106.heracles.sohuno.com:50075/webhdfs/v1/user/sohuvideo/online/srcFile/188/718/188718422/dat1_188718422_2020_4_11_17_3_1726460c504.mp4?op=OPEN&user.name=sohuvideo&namenoderpcaddress=sotocyon&offset=0')
    # print('time', time.time()-begin)
    #
    # begin = time.time()
    # local_filename = download_file('http://sdn077106.heracles.sohuno.com:50075/webhdfs/v1/user/sohuvideo/online/srcFile/188/718/188718422/dat1_188718422_2020_4_11_17_3_1726460c504.mp4?op=OPEN&user.name=sohuvideo&namenoderpcaddress=sotocyon&offset=0')
    # print('time', time.time()-begin)

    begin = time.time()
    local_filename = download_file('http://10.19.17.188:10086/zhangyang/pacific.rim.mp4')
    print('time2', time.time() - begin)

