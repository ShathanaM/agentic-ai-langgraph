from app.tools.search_tool import search_tool
from app.rag.pdf_qa import ask_pdf
from app.rag.rag_manager import get_vectorstore

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def multi_tool_agent(question):

    # Search Internet
    search_result = search_tool(question)

    # Search PDF
    vectorstore = get_vectorstore()

    pdf_result = ""

    if vectorstore:
        pdf_result = ask_pdf(
            vectorstore,
            question
        )

    prompt = f"""
You are an AI analyst.

Use BOTH sources below.

Internet Information:
{search_result}

PDF Information:
{pdf_result}

User Question:
{question}

Give a combined answer.
"""

    response = llm.invoke(prompt)

    return response.content