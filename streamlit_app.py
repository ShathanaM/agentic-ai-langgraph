import streamlit as st

from app.graph.workflow import graph
from app.rag.load_pdf import load_pdf

st.set_page_config(
    page_title="Agentic AI",
    page_icon="🤖"
)

st.title("🤖 Agentic AI Assistant")

if "loaded" not in st.session_state:
    load_pdf()
    st.session_state.loaded = True

query = st.text_input(
    "Ask something:"
)

if st.button("Submit"):

    result = graph.invoke(
        {
            "user_input": query
        }
    )

    st.write("### Response")
    st.write(result["final_response"])