# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 12:33
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

class Test(object):
    def __enter__(self):
        print 'enter'
        return self

    def __exit__(self, type, value, traceback):
        print type, value, traceback
        print 'exit'

    def func(self):
        print 'hi'

with Test() as t:
    t.func()

print '------------------'

try:
    with Test() as t:
        raise Exception('test exception')
        t.func()
except Exception as e:
    print e

print '------------------'

def test_return():
    with Test() as t:
        return 'end before func'
        t.func()

def test_return2():
    with Test() as t:
        t.func()
        return 'end after func'

test_return()
test_return2()