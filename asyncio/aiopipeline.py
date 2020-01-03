# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 12:29
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import asyncio

class MyException(Exception):
    pass

class Pipeline(object):
    def __init__(self):
        self.source = None

    def __iter__(self):
        return self.generator()

    def generator(self):
        while self.has_next():
            data = next(self.source) if self.source else {}
            if self.filter(data):
                yield self.map(data)

    def __or__(self, other):
        other.source = self.generator()
        return other

    def filter(self, data):
        return True

    def map(self, data):
        return data

    def has_next(self):
        return True

class AioPipeline(object):
    def __init__(self):
        self.source = None

    def __aiter__(self):
        return self.generator()

    async def generator(self):
        try:
            # while self.has_next():
            async for data in self.source:
                if not self.has_next():
                    return
            #data = next(self.source) if self.source else {}
                if await self.filter(data):
                    yield await self.map(data)

        except StopAsyncIteration:
            return

    def __or__(self, other):
        other.source = self.generator()
        return other

    async def filter(self, data):
        return True

    async def map(self, data):
        return data

    def has_next(self):
        return True


class AllNumbers(AioPipeline):
    async def generator(self):
        value = 0
        while True:
            yield value
            value += 1


class Evens(AioPipeline):
    async def filter(self, value):
        return value % 2 == 0


class MultipleOf(AioPipeline):
    def __init__(self, factor=1):
        self.factor = factor
        super(MultipleOf, self).__init__()

    async def filter(self, value):
        return value % self.factor == 0


class Printer(AioPipeline):
    async def map(self, value):
        print(value)
        return value


class First(AioPipeline):
    def __init__(self, total=10):
        self.total = total
        self.count = 0
        super(First, self).__init__()

    async def map(self, value):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count > self.total:
            #raise MyException('test')
            raise StopAsyncIteration
        return value


async def aio_drain(pipeline):
    async for _ in pipeline:
        pass

async def main():
    all_numbers = AllNumbers()
    evens = MultipleOf(2)
    multiple_of_3 = MultipleOf(3)
    printer = Printer()
    first_10 = First(10)

    try:
        # a | b, a b still are sequential
        pipeline = all_numbers | evens | multiple_of_3 | first_10 | printer
        await aio_drain(pipeline)

    except MyException as e:
        print('catch %s' % e)


if __name__ == '__main__':
    c_main = main()
    asyncio.run(c_main)