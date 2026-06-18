def router(state):

    query = state["user_input"].lower()

    if "what is my name" in query:
        return {"route": "memory"}

    if any(word in query for word in [
        "pdf",
        "document",
        "resume",
        "file"
    ]):
        return {"route": "pdf"}

    if any(op in query for op in [
        "+", "-", "*", "/"
    ]):
        return {"route": "calculator"}

    return {"route": "search"}