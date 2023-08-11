from pydantic import BaseModel

from.OdArgs import ODArgs

class OdRequest(BaseModel):
    image_bytes: bytes
    args: ODArgs