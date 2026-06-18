from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_tool(query):

    response = client.search(
        query=query,
        max_results=5
    )

    if response.get("results"):
        return response["results"][0]["content"]

    return "No search results found."