# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 19:43
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

class TestExecutor():
    def __init__(self):
        self.exit_flag = False

    async def print_hello(self):
        while not self.exit_flag:
            print('hello')
            await asyncio.sleep(1)

    def do_something(self):
        time.sleep(3)
        self.exit_flag=True

    async def main(self):
        h = self.print_hello()
        print(type(h))

        loop = asyncio.get_running_loop()

        d = loop.run_in_executor(None, self.do_something)
        print(type(d))

        await asyncio.gather(h, d)

if __name__ == '__main__':
    t = TestExecutor()
    asyncio.run(t.main())