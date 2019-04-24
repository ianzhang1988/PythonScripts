#coding=utf-8

import requests
import time

def ftp_server():
    url = 'http://api.inner.tv.sohuno.com/outapi/ftp/getFtpServerIp2.do?from=1'
    rep = requests.post(url)
    print(rep.text)

# ftp_server()

def test_face_db():
    data = {
    'list':[
            {   'group_id':'test',
                'person_id':'2000004',
                'img_path':['/opt/ipc_1/face_db_pic/10001/known/adcc168f95d5498b939fd6eceea9ab9e_1542251192000.jpg'],
                },
        #/opt/zhangyang/10003.jpg
            # {   'group_id':'test',
            #     'person_id':'2000002',
            #     'img_path':['/opt/ipc_1/pic/2000002/00001.jpg','/opt/ipc_1/pic/2000002/00002.jpg'],
            # },
        ],
    }

    url = 'http://10.18.18.68:6789/featureadd'
    rep = requests.post(url,json=data, timeout=5)
    print(rep.text)

#test_face_db()

# 1072106375219576832
def test_face_db_del():
    data = {
    'list':[
            {   'group_id':'10001',
                'person_id':'1072107501180485632',
                },
        #/opt/zhangyang/10003.jpg
            # {   'group_id':'test',
            #     'person_id':'2000002',
            #     'img_path':['/opt/ipc_1/pic/2000002/00001.jpg','/opt/ipc_1/pic/2000002/00002.jpg'],
            # },
        ],
    }

    url = 'http://10.18.18.68:6789/featuredelete'
    rep = requests.post(url,json=data, timeout=5)
    print(rep.text)

# test_face_db_del()

def test_trans_face():
    data = {
    'video_id':'90367798',
    'fps':30,
    #'length':5,
    # 'input_file':'./cage.jpg',
    'pic_url':'http://10.10.76.179:7777/testpic/cage.jpg',
    #'video_output': './testout/output',
    #'trans_width': '360',
    #'trans_height': '885',
    #'bitrate': '500k',
    'template_id':'2'
}

    url = 'http://10.10.92.190:8888/face'
    requests.post(url, json=data, timeout=5)

#test_trans_face()


def test_DNA_poolitem():
    data = {
    'pool_name':'VR',
    }

    url = 'http://10.16.50.156:9999/poolitem'
    rep = requests.get(url, json=data, timeout=5)
    print(rep.status_code)
    print(rep.json())

#test_DNA_poolitem()

def shafa_download():
    url='http://10.19.16.64:7000/download?vid=%s'
    url = url % '121940373'
    rep = requests.get(url, timeout=10)
    print(rep.status_code)
    print(rep.json())

def shafa_status():
    url = 'http://10.19.16.64:7000/status?vid=%s'
    url = url % '121940373'
    rep = requests.get(url, timeout=10)
    print(rep.status_code)
    print(rep.json())

#shafa_download()
#shafa_status()

def ugc_cdn_download():
    url='http://10.16.50.148:7000/download?vid=%s'
    url = url % '126082970'
    rep = requests.get(url, timeout=10)
    print(rep.status_code)
    print(rep.json())

def ugc_cdn_status():
    url = 'http://10.16.50.148:7000/status?vid=%s'
    url = url % '126082970'
    rep = requests.get(url, timeout=10)
    print(rep.status_code)
    print(rep.json())

ugc_cdn_download()
time.sleep(5)
ugc_cdn_status()