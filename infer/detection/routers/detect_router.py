import traceback
from fastapi import File, Form, UploadFile
from web.router_registry import routerRegistry
from ..services.detect_service import detectService
import time

router = routerRegistry.new_router("/infer/od")

@router.post("/yolov8")
async def yolo_od(fileb: UploadFile = File(...), token: str = Form(...)):
    try:
        result = detectService.detect(fileb)
        print(result)
        return {
            "token": token,
            "filename": fileb.filename,
            "content_type": fileb.content_type,
            "result": result
        }
    except:
        traceback.print_exc()
        return -1
