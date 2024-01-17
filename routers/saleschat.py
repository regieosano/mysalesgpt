from fastapi import HTTPException, status
from routers.route.router import post_router
from models.schemas import PostSalesChat, PostSalesChatResponse
from services.api.saleschat import SaleChatService

sales_chat_service = SaleChatService()


@post_router.post(
    "/saleschat", status_code=status.HTTP_200_OK, response_model=PostSalesChatResponse
)
def chat_sales_query(post_chat_sales_question: PostSalesChat):
    try:
        answer = sales_chat_service.get_ai_chat_sales_answer(post_chat_sales_question)
        return PostSalesChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
