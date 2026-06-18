from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from app.memory.memory import get_all_memory
from app.memory.chat_history import (
    add_message,
    get_history
)

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def responder(state):

    user_input = state.get("user_input", "")
    plan = state.get("plan", "")
    tool_result = state.get("tool_result", "")

    memory = get_all_memory()
    history = get_history()

    prompt = f"""
You are a helpful AI assistant.

Conversation History:
{history}

User Question:
{user_input}

Plan:
{plan}

Memory:
{memory}

Tool Result:
{tool_result}

Instructions:
- Use the tool result when available.
- Use memory when relevant.
- Use conversation history for context.
- Give a natural and helpful response.
"""

    response = llm.invoke(prompt)

    add_message("user", user_input)
    add_message("assistant", response.content)

    return {
        "final_response": response.content
    }