# coding=utf-8

import random, string
import requests
import ftplib

def gen_rand_str(num):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt



print gen_rand_str(10)

