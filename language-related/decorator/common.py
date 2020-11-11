# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 15:52
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from functools import wraps

class bar:
    def deco1(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print('calling', func.__name__)
            return func(self, *args, **kwargs)

        return wrapper

    def deco2(action):
        def deco2_(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                print('calling', func.__name__, 'action:', action)
                return func(self, *args, **kwargs)
            return wrapper
        return deco2_

    @deco1
    def fun1(self):
        print('this is fun1')

    @deco1
    def fun2(self, a):
        print('this is fun2',a)

    @deco2('test')
    def fun3(self, b):
        print('this is fun3',b)


b = bar()
b.fun1()
b.fun2('hi')
b.fun3('nihao')