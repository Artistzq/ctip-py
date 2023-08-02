import time
import base64

from fastapi import UploadFile

class DetectService:

    def __init__(self) -> None:
        pass
    
    async def detect(self, img: UploadFile):
        img_bytes = await img.read()
        time.sleep(1.5)
        return base64.b64encode(img_bytes)

detectService = DetectService()