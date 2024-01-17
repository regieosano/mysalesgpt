from langchain.chains import LLMChain
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from models.schemas import PostSalesMessage
from salesgpt.prompts import SALES_AGENT_ROLES
from memory.conversation import conversation_memory
from openaimodels.llm_models import chat


class SalesChatService:
    def get_ai_chat_sales_answer(self, content: PostSalesMessage):
        chat_prompt = ChatPromptTemplate(
            input_variables=["content", "messages"],
            messages=[
                MessagesPlaceholder(variable_name="messages"),
                SystemMessagePromptTemplate.from_template(SALES_AGENT_ROLES),
                HumanMessagePromptTemplate.from_template(content.message),
            ],
        )

        chain = LLMChain(llm=chat, prompt=chat_prompt, memory=conversation_memory)

        result = chain.invoke({"content": content.message})
        return {"answer": result["text"]}
