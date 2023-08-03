import traceback
from typing import AnyStr
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, parse_obj_as

from ..models.StableDiffusionArgs import StableDiffusionArgs
from web.router_registry import routerRegistry
from ..services.text2img_service import textToImageService


router = routerRegistry.new_router("/infer/to_img")

@router.post("/text2img_sync")
async def text2img(sd_arg: StableDiffusionArgs):
    return textToImageService.text2img(sd_arg)