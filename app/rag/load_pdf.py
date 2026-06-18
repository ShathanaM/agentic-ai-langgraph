from app.tools.pdf_tool import read_pdf
from app.rag.text_splitter import split_text
from app.rag.vector_store import create_vector_store
from app.rag.rag_manager import set_vectorstore

def load_pdf():

    text = read_pdf("sample.pdf")

    chunks = split_text(text)

    vectorstore = create_vector_store(chunks)

    set_vectorstore(vectorstore)

    print("PDF Loaded Successfully")