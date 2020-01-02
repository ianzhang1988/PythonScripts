# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 12:29
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import asyncio

class Pipeline(object):
    def __init__(self):
        self.source = None

    def __aiter__(self):
        return self.generator()

    async def generator(self):
        try:
            # while self.has_next():
            async for data in self.source:
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


class AllNumbers(Pipeline):
    async def generator(self):
        value = 0
        while True:
            yield value
            value += 1


class Evens(Pipeline):
    async def filter(self, value):
        return value % 2 == 0


class MultipleOf(Pipeline):
    def __init__(self, factor=1):
        self.factor = factor
        super(MultipleOf, self).__init__()

    async def filter(self, value):
        return value % self.factor == 0


class Printer(Pipeline):
    async def map(self, value):
        print(value)
        return value


class First(Pipeline):
    def __init__(self, total=10):
        self.total = total
        self.count = 0
        super(First, self).__init__()

    async def map(self, value):
        self.count += 1
        if self.count > self.total:
            raise StopAsyncIteration
        return value


async def main():
    all_numbers = AllNumbers()
    evens = MultipleOf(2)
    multiple_of_3 = MultipleOf(3)
    printer = Printer()
    first_10 = First(10)

    pipeline = all_numbers | evens | multiple_of_3 | first_10 | printer

    async for i in pipeline:
        pass


if __name__ == '__main__':
    c_main = main()
    asyncio.run(c_main)