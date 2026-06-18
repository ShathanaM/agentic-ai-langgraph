 Agentic AI System using LangGraph

Project Overview:
This project is an AI-powered Agentic system built using LangGraph, LangChain, and Python.

It can understand user queries and intelligently route them to different tools such as:
- Calculator tool 
- Web search tool 
- PDF Question Answering (RAG system) 
- Memory-based conversation 
- Multi-tool AI agent 

The system uses an LLM-based router to decide which tool should handle the user query.


 Tech Stack
- Python 
- LangChain 
- LangGraph 
- Streamlit 
- FAISS (Vector Database) 


How the System Works

User Input  
→ LLM Router decides tool  
→ Tool executes task  
→ Final response is generated  

Tools include:
- Calculator
- Search Engine
- PDF QA (RAG)
- Memory system
- Agent executor

 Project Structure

agentic-ai-langgraph/
│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── memory/
│   ├── rag/
│   ├── tools/
│   └── state/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── sample.pdf
└── README.md


Architecture Diagram

The system is designed as a modular AI agent pipeline using LangGraph.

                ┌─────────────────────┐
                │     User Input      │
                └─────────┬───────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   LLM Router Node    │
              │ (Intent Detection)   │
              └─────────┬────────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ Calculator  │ │ Web Search   │ │   PDF RAG    │
│   Tool      │ │   Tool       │ │  Retriever   │
└─────┬───────┘ └─────┬────────┘ └─────┬────────┘
      │               │                │
      └───────────────┴────────────────┘
                      ▼
           ┌────────────────────┐
           │ Response Generator  │
           │ (LLM Final Answer)  │
           └─────────┬──────────┘
                     ▼
             ┌──────────────┐
             │  Streamlit UI │
             └──────────────┘


Deployment

This application is deployed as a lightweight Streamlit web app.

The system is designed to run as a stateless frontend with backend AI processing handled through LangGraph workflows.

Deployment Environment
- Frontend: Streamlit
- Backend: Python (LangGraph runtime)
- Model Layer: LLM API integration

Production Flow
- Code is pushed to GitHub
- Streamlit Cloud reads repository
- `streamlit_app.py` acts as entry point
- Dependencies are installed from `requirements.txt`
- Application runs as a web service

  
Features
- Intelligent query routing
- Multi-tool AI system
- PDF-based Q&A (RAG)
- Memory-based chat system
- Streamlit UI interface

What I learned

While building this project, I learned how modern AI agent systems are structured beyond simple LLM calls.

Instead of relying on a single model response, real-world systems use:
- Routing layers for decision making
- Modular tool execution
- Memory integration for context retention
- Retrieval systems for external knowledge (RAG)

This approach significantly improves flexibility, scalability, and real-world usability of AI applications.


 Author:
Shathana M  
AI/ML Developer | LangGraph & LLM Systems
