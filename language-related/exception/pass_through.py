# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 10:43
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import traceback

class MyException(Exception):
    pass

def test_sub():
    raise MyException('test')

def test():
    exception = None
    try:
        test_sub()
    except Exception as e:
        # raise e
        exception = e

    raise exception

def main():
    try:
        test()
    except Exception as e:
        print(type(e),str(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()