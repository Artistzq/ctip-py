import io
from PIL import Image
from fastapi.responses import StreamingResponse
import numpy as np

from ..models.StableDiffusionArgs import StableDiffusionArgs


class TextToImageService:
    
    def img2response(self, np_array: np.ndarray):
        # 将图像数组转换为PIL图像对象
        image = Image.fromarray(np_array)

        # 将图像转换为字节流
        buffer = io.BytesIO()
        image.save(buffer, format='png')
        buffer.seek(0)

        return StreamingResponse(io.BytesIO(buffer.read()), media_type="image/jpeg")
        
        
    def text2img(self, args: StableDiffusionArgs):
        # 生成图像数据，这里使用示例数据
        print(args)

        # 创建图像数组
        width, height = 512, 768
        image_data = np.zeros((height, width, 3), dtype=np.uint8)
        image_data[:, :, 0] = 120  # 设置红色通道为最大值，表示红色
        image_data[:, :, 1] = 0    # 设置绿色通道为0，表示没有绿色
        image_data[:, :, 2] = 0    # 设置蓝色通道为0，表示没有蓝色

        return self.img2response(image_data)
    
textToImageService = TextToImageService()