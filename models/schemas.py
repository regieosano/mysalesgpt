from pydantic import BaseModel


class PostSalesChat(BaseModel):
    question: str


class PostSalesChatResponse(BaseModel):
    answer: str
