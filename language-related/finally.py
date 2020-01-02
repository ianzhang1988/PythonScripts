# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 18:13
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

def test_return():
    try:
        raise Exception('test')
    except Exception as e:
        print('before return')
        return
    finally:
        print('got here even after return')

def test_for():
    for i in range(5):
        try:
            print(i)
            if i == 2:
                raise Exception('a')
            if i == 3:
                raise Exception('b')
        except Exception as e:
            print(str(e))
            if str(e) == 'a':
                continue
            if str(e) == 'b':
                break
        finally:
            print('----- else here',i)

def test_2_try():
    try:
        try:
            raise Exception('exc')
        except Exception as e:
            print('inner catch exception')
    except Exception as e:
        print('outer catch exception')
    finally:
        print('1st try finally')

if __name__ == '__main__':
    test_return()
    test_for()
    test_2_try()
