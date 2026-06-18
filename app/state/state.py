from typing import TypedDict

class AgentState(TypedDict, total=False):

    user_input: str

    route: str

    plan: str

    tool_result: str

    final_response: str

    memory: str

    chat_history: list