from fastapi import APIRouter

class RouterResgistry:
    
    def __init__(self) -> None:
        self.routers = {}

    def new_router(self, prefix):
        router = APIRouter()
        self.routers[prefix] = router
        return router

routerRegistry = RouterResgistry()