from langgraph.graph import StateGraph, END

from app.state.state import AgentState

from app.agents.responder import responder
from app.agents.memory_agent import memory_agent
from app.agents.router import router
from app.agents.tool_executor import tool_executor
from app.agents.llm_router import llm_router
from app.agents.planner import planner

builder = StateGraph(AgentState)

builder.add_node("memory", memory_agent)
builder.add_node("planner", planner)
builder.add_node("router", llm_router)
builder.add_node("tool_executor", tool_executor)
builder.add_node("responder", responder)

builder.set_entry_point("memory")

builder.add_edge("memory", "planner")
builder.add_edge("planner", "router")
builder.add_edge("router", "tool_executor")
builder.add_edge("tool_executor", "responder")
builder.add_edge("responder", END)

graph = builder.compile()