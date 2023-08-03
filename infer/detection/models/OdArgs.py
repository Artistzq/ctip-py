from pydantic import BaseModel

class ODArgs(BaseModel):
    id: int
    name = "default"