# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 18:15
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}