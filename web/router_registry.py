from fastapi import APIRouter

class RouterResgistry:
    
    def __init__(self) -> None:
        self.routers = {}

    def new_router(self, name):
        router = APIRouter()
        self.routers[name] = router
        return router

routerRegistry = RouterResgistry()