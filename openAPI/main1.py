from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
# local
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'), ssl_cert_reqs="none")
# render.com
# redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
# 沒有加可以是字串，加 int 需 數字
async def read_item(item_id:int):
    print(f"使用者輸入了 {item_id}")
    return {"item_id": item_id}


@app.get("/items/{date}/{celsius}")
async def get_item(date:str,celsius:float):
    print(f"日期:{date}")
    print(f"溫度:{celsius}")
    return {"日期":date,"攝氏溫度":celsius}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/pico_w/{date}")
async def read_item(date:str, address:str, celsius:float, light:float):
    print(f"日期:{date}")
    print(f"地址:{address}")
    print(f"溫度:{celsius}")
    print(f"光線:{light}")
    return {"日期":date,"地址":address,"攝氏溫度":celsius,"光線":light}


@app.get("/pico_w/{date}")
async def read_item(date:str, address:str, celsius:float=0.0):
    print(f"日期:{date}")
    print(f"地址:{address}")
    print(f"溫度:{celsius}")
    return {"日期":date,"地址":address,"攝氏溫度":celsius}