from fastapi import HTTPException, status
from routers.route.router import post_router
from models.schemas import PostSalesMessage, PostSalesMessageResponse
from services.api.saleschat import SalesChatService

sales_chat_service = SalesChatService()


@post_router.post(
    "/saleschat",
    status_code=status.HTTP_200_OK,
    response_model=PostSalesMessageResponse,
)
def chat_sales_query(message: PostSalesMessage):
    try:
        answer = sales_chat_service.get_ai_chat_sales_answer(message)
        return answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
