from app.graph.workflow import graph
from app.rag.load_pdf import load_pdf

load_pdf()

while True:

    query = input("Ask: ")

    result = graph.invoke(
        {
            "user_input": query
        }
    )

    print("\n")
    print(result["final_response"])
    print("\n")