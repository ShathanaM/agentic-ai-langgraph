from app.tools.search_tool import search_tool

def executor(state):

    query = state["user_input"]

    result = search_tool(query)

    return {
        "tool_result": result
    }