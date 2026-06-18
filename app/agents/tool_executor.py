from app.memory.memory import get_memory
from app.tools.calculator_tool import calculator_tool
from app.tools.search_tool import search_tool
from app.agents.multi_tool_agent import multi_tool_agent
from app.rag.pdf_qa import ask_pdf
from app.rag.rag_manager import get_vectorstore


def tool_executor(state):

    route = state.get("route", "search")
    query = state["user_input"]

    if route == "memory":

        name = get_memory("name")

        return {
            "tool_result": f"User name is {name}"
        }

    elif route == "calculator":

        return {
            "tool_result": calculator_tool(query)
        }

    elif route == "pdf":

        vectorstore = get_vectorstore()

        if vectorstore is None:
            return {
                "tool_result": "PDF not loaded."
            }

        answer = ask_pdf(
            vectorstore,
            query
        )

        return {
            "tool_result": answer
        }

    elif route == "multi":

        answer = multi_tool_agent(query)

        return {
            "tool_result": answer
        }

    else:

        return {
            "tool_result": search_tool(query)
        }