import os
import sys
from fastapi import FastAPI
import uvicorn
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import detection # 注入
import to_img # 注入
import config
from util.nacos_util import nacosRegister
from web.router_registry import routerRegistry
from infer.to_img.mq.text2img_consumer import start_kafka_consumers, stop_kafka_consumers

app = FastAPI()
# 注册路由
for prefix, router in routerRegistry.routers.items():
    print(prefix)
    app.include_router(router, prefix=prefix)
# 注册服务
nacosRegister.register_new_service_from_config(config)

@app.on_event("startup")
async def startup_event():
    # 创建并启动多个线程来处理Kafka消息
    app.kafka_threads = start_kafka_consumers(config.kafka.topic, config.kafka.bootstrap_servers, config.kafka.num_threads)

@app.on_event("shutdown")
async def shutdown_event():
    # 取消所有Kafka消费任务并等待它们结束s
    stop_kafka_consumers(app.kafka_threads)

if __name__ == '__main__':
    uvicorn.run(app="app:app", host=config.host, port=config.port, reload=True)

