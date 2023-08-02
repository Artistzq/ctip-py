import os
import sys
from fastapi import FastAPI
import uvicorn
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
import detection
import text2img


app = FastAPI()

from web.router_registry import routerRegistry

for prefix, routers in routerRegistry.routers.items():
    app.include_router(routers, prefix=prefix)

# from util.nacos_util import nacosRegister
# nacosRegister.register_new_service(
#     service_name='ctip-py-service',
#     ip=config.host,
#     port=config.port
# )


if __name__ == '__main__':
    uvicorn.run(app="app:app", host=config.host, port=config.port, reload=True)

