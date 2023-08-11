import traceback
from typing import AnyStr
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, parse_obj_as
import time
import json

from web.router_registry import routerRegistry
from ..services.detect_service import detectService
from ..models.OdArgs import ODArgs
from ..models.OdRequest import OdRequest

router = routerRegistry.new_router("/infer/od")

@router.post("/yolov8")
async def yolo_od(fileb: UploadFile, args: str = Form(...)):
    try:
        args = parse_obj_as(ODArgs, json.loads(args))
        return detectService.detect(fileb, args)
    except:
        traceback.print_exc()
        return -1

@router.post("/yolov8_bytes")
async def yolo_od_bytes(bytes: AnyStr, args: str=Form(...)):
    try:
        args = parse_obj_as(ODArgs, json.loads(args))
        return detectService.detect_from_bytes(bytes, args)
    except:
        traceback.print_exc()
        return -1
    
@router.post("/yolov8_request_body")
async def yolo_od_bytes(odRequest: OdRequest):
    try:
        bytes = odRequest.image_bytes
        args = parse_obj_as(ODArgs, json.loads(odRequest.args))
        return detectService.detect_from_bytes(bytes, args)
    except:
        traceback.print_exc()
        return -1