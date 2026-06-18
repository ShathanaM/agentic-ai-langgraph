from app.memory.memory import save_memory

def memory_agent(state):

    query = state["user_input"]

    if "my name is" in query.lower():

        name = query.split("is")[-1].strip()

        save_memory("name", name)

        return {
            "memory": f"Saved name: {name}"
        }

    return {}