from pydantic import BaseModel


class PostSalesMessage(BaseModel):
    message: str


class PostSalesMessageResponse(BaseModel):
    answer: str
