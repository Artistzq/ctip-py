import time
import base64
import io
from PIL import Image, ImageDraw

from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse

from ..models.OdArgs import ODArgs

class DetectService:
    
    def detect(self, img_file: UploadFile, args: ODArgs):
        
        # 读取上传的图像数据
        image_bytes = img_file.file.read()

        # 将图像转换为PIL对象
        image = Image.open(io.BytesIO(image_bytes))

        # 在图像上画一个圆圈
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        circle_center = (image_width // 2, image_height // 2)
        circle_radius = min(image_width, image_height) // 4
        draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                    circle_center[0] + circle_radius, circle_center[1] + circle_radius), fill=None, outline="red", width=5)

        # 将处理后的图像保存到字节流
        output_image_stream = io.BytesIO()
        image.save(output_image_stream, format="JPEG")
        output_image_stream.seek(0)

        # 返回处理后的图像
        return StreamingResponse(io.BytesIO(output_image_stream.read()), media_type="image/jpeg")


detectService = DetectService()