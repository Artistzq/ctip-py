from pydantic import BaseModel

class StableDiffusionArgs(BaseModel):
    prompt: str
    neg_prompt: str = ""