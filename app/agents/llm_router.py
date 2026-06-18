from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def llm_router(state):

    query = state["user_input"]

    prompt = f"""
You are a routing agent.

Available routes:

memory
calculator
pdf
search
multi

User Query:
{query}

Return ONLY one word:
memory
calculator
pdf
search
multi
"""

    response = llm.invoke(prompt)

    route = response.content.strip().lower()

    # Override with multi route for comparison/trend queries
    multi_keywords = ["compare", "comparison", "trend", "both"]

    if any(keyword in query.lower() for keyword in multi_keywords):
        route = "multi"

    print("LLM ROUTE:", route)

    return {
        "route": route
    }