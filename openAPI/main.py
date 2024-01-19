from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
load_dotenv()
# local
# redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'), ssl_cert_reqs="none")
# render.com
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment')
    return {"counter": counter}


@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_conn.incr('test:increment',c)
    return {"counter": counter}


@app.get("/temperature/{c}")
def temperature(c:int):
    counter = redis_conn.incr('test:increment',c)
    return {"counter": counter}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}