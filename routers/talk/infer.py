from pydantic import BaseModel

from .router_talk import talk_router


class MsgDTO(BaseModel):
    talkContent: str
    id: int


@talk_router.post("/infer")
async def talk_infer(msg: MsgDTO):
    msg.talkContent += " processed"
    return msg

