# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 20:25
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

class Field(object):
    def __init__(self,name):
        self.name = name
        self.internal_name = '_'+self.name

    def __set__(self,instance, value):
        if instance is None:
            return self
        print('set',instance)
        setattr(instance,self.internal_name, value)

    def __get__(self, instance, owner):
        print('get', instance)
        return getattr(instance,self.internal_name)

class Test(object):
    a = Field('a')


if __name__ == "__main__":

    a = Field('a')
    a.test = 'hi'
    a.a='h2'
    print(a.__dict__)
    print(a.test)

    t = Test()
    t.a='hi3'
    print(type(t.a))
    t.a = 'hi3.1'
    t.a = 'hi3.2'
    print(t.a)
    print(t.a)
    t.test='hi4'
    print(t.test)
    print(t.__dict__)
