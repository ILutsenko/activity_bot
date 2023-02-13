from pydantic import BaseModel


class MessageModel(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    full_name: str
    username: str
