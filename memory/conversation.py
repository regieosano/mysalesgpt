from langchain.memory import ConversationSummaryMemory
from openai import chat
from memory import file_chat_messages

conversation_memory = ConversationSummaryMemory(
    chat_memory=file_chat_messages,
    memory_key="messages",
    return_messages=True,
    llm=chat,
)
