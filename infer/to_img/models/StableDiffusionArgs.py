from pydantic import BaseModel

class StableDiffusionArgs(BaseModel):
    prompt: str
    negativePrompt: str = ""