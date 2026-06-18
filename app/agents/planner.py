from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def planner(state):

    question = state["user_input"]

    prompt = f"""
You are an expert planning agent.

Create a step-by-step plan for:

{question}

Return only the plan.
"""

    response = llm.invoke(prompt)

    print("\nPLAN:")
    print(response.content)
    print()

    return {
        "plan": response.content
    }