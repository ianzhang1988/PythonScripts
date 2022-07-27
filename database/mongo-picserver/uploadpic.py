# coding:utf-8

import os
import requests
from concurrent.futures import ThreadPoolExecutor

pic_server='http://127.0.0.1:3000/put'

def upload(args):
    file, id, name = args
    # print file
    with open(file,'rb') as f:
        files = {'file': f}
        rep = requests.post(pic_server,files = files, params={'id':id, 'name':name}, headers={'Connection':'close'})
        if rep.status_code != requests.codes.ok:
            print 'upload',file,'failed'

base_pic_dir = '/opt/vr-picdb/0/114'

pic_file_path = open('picfile.txt','w')

pool = ThreadPoolExecutor(20)

for dir1 in os.listdir(base_pic_dir):
    path1 = os.path.join(base_pic_dir, dir1)
    if not os.path.isdir(path1):
        continue
    for dir2 in os.listdir(path1): # id
        path2 = os.path.join(path1, dir2)
        if not os.path.isdir(path2):
            continue
        vid = dir2[:-2] # remove '_0'
        #pic_files = []
        for file in os.listdir(path2): #files
            if 'jpg' not in file:
                continue
            path3 = os.path.join(path2,file)
            #pic_files.append((path3,vid,file)) # file, id, file name
            pool.submit(upload, (path3,vid,file))
            pic_file_path.write('%s\n'%path3)
        #pool.map(upload, pic_files)

pool.shutdown()

pic_file_path.close()