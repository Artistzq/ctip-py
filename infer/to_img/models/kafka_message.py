from pydantic import BaseModel
from datetime import datetime

class KafkaMessage(BaseModel):
    message: str
    code: int
    data: object
    time: datetime
    messageId: str