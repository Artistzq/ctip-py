from fastapi import FastAPI
from routers import *
from nacos import NacosClient
import uvicorn
import time

app = FastAPI()

app.include_router(talk_router, prefix="/talk")

# uvicorn.run("main:app", host="127.0.0.1", port=7999, log_level="info")

# 创建Nacos客户端并连接到Nacos服务器
client = NacosClient('localhost:8848')

# 注册服务
client.add_naming_instance(
    service_name='ctip-py-service',
    ip='127.0.0.1',
    port=7999
)

# 定义心跳函数
def heartbeat():
    while True:
        # 向Nacos发送心跳
        client.send_heartbeat('ctip-py-service', '127.0.0.1', 7999)
        time.sleep(5)  # 每隔5秒发送一次心跳
        print("heat beat.")

# 启动心跳线程
import threading
thread = threading.Thread(target=heartbeat)
thread.start()
