# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 12:38
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")